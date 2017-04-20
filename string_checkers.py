"""
Additional Pylint checkers for string formatting operations.
"""


import tokenize

from pylint.checkers import BaseTokenChecker
from pylint.interfaces import ITokenChecker


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
           }
    options = (('expected-string-literal-quote',
                {'type': 'choice', 'metavar': '<\' or ">', 'default': '\'',
                 'choices': ['\'', '"'],
                 'help': 'The default string literal quote character. Must be '
                         'either \' or "'}),
              )

    def process_tokens(self, tokens):
        for tok_type, token, (start_row, _), _, _ in tokens:
            if tok_type == tokenize.STRING:
                self._process_string_token(token, start_row)

    def _process_string_token(self, token, start_row):
        # Adapted from pylint/checkers/strings.py
        for i, c in enumerate(token):
            if c in ('\'', '"'):
                quote_char = c
                break

        # pylint: disable=undefined-loop-variable
        # We ignore prefix markers like u, b, r
        after_prefix = token[i:]

        # Ignore triple quoted strings
        if len(after_prefix) >= 3 and after_prefix[:3] in ('\'\'\'', '"""'):
            return

        quote_char = after_prefix[0]
        expected_quote_char = self.config.expected_string_literal_quote

        if quote_char != expected_quote_char:
            self.add_message('incorrect-string-literal-quote',
                             line=start_row,
                             args=(expected_quote_char, quote_char))


def register(linter):
    linter.register_checker(LiteralQuoteChecker(linter))
