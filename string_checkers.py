"""
Additional Pylint checkers for string formatting operations.
"""


import tokenize

from pylint.checkers import BaseTokenChecker
from pylint.interfaces import ITokenChecker


SINGLE_QUOTES = ('\'', '"')
TRIPLE_QUOTES = ('\'\'\'', '"""')

DEFAULT_SINGLE_QUOTE = '\''
DEFAULT_TRIPLE_QUOTE = '"""'


class LiteralQuoteChecker(BaseTokenChecker):
    """
    Check that string literals use a consistent quote character, be it a single
    quote or a double quote.
    """

    __implements__ = ITokenChecker

    name = 'string_literal_quotes'
    msgs = {'C8001': ('Use quote character `%s` for string literals, not '
                      '`%s`.',
                      'incorrect-string-literal-quote',
                      'Used when the string literal quote character does not '
                      'match the one specified in the '
                      '`expected-string-literal-quote` option.'),
            'C8002': ('Use `%s` triple-quotes, not `%s`.',
                      'incorrect-triple-quotes',
                      'Used when the triple-quotes character does not match '
                      'the one specified in the `expected-triple-quote` '
                      'option.'),
           }
    options = (('expected-string-literal-quote',
                {'type': 'choice', 'metavar': '<\' or ">',
                 'default': DEFAULT_SINGLE_QUOTE, 'choices': SINGLE_QUOTES,
                 'help': 'The default string literal quote character. Must be '
                         'either \' or "'}),
               ('expected-string-triple-quote',
                {'type': 'choice', 'metavar': '<\'\'\' or """>',
                 'default': DEFAULT_TRIPLE_QUOTE, 'choices': TRIPLE_QUOTES,
                 'help': 'The default string triple quote. Must be either '
                         '\'\'\' or """'}),
              )

    def process_tokens(self, tokens):
        for tok_type, token, (start_row, _), _, _ in tokens:
            if tok_type == tokenize.STRING:
                self._process_string_token(token, start_row)

    def _process_string_token(self, token, start_row):
        expected_quote_char = self.config.expected_string_literal_quote
        expected_triple_quotes = self.config.expected_string_triple_quote

        # Adapted from pylint/checkers/strings.py
        for i, c in enumerate(token):
            if c in SINGLE_QUOTES:
                break

        # pylint: disable=undefined-loop-variable
        # We ignore prefix markers like u, b, r
        after_prefix = token[i:]

        # Check triple-quote strings
        if len(after_prefix) >= 3 and after_prefix[:3] in TRIPLE_QUOTES:
            if after_prefix[:3] != expected_triple_quotes:
                self.add_message('incorrect-triple-quotes',
                                 line=start_row,
                                 args=(expected_triple_quotes, after_prefix[:3]))
        # Check single quote strings
        elif after_prefix[0] != expected_quote_char:
            self.add_message('incorrect-string-literal-quote',
                             line=start_row,
                             args=(expected_quote_char, after_prefix[0]))


def register(linter):
    linter.register_checker(LiteralQuoteChecker(linter))
