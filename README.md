# Pylint String Checkers

Additional string checkers for [Pylint](https://pylint.org).

## Install

```
git clone https://github.com/adrianherrera/pylint-string-checkers.git
cd pylint-string-checkers
pip install .
```

## Usage

To use the additional string checkers, run Pylint as follows:

```
pylint --load-plugins string_checkers foo.py
```

## Checkers

### String literal quotes

Most Python style guides (e.g.
[Google's](https://google.github.io/styleguide/pyguide.html#Strings)) allow
either single or double quote characters for string literals. What is more
important is that you remain consistent. This checker allows you to specify
(via the `expected-string-literal-quote` option) whether to use single or
double quote characters for string literals.

### String concatenation

String substitution is often recommended over string concatenation. This checker
will find string concatenation operations that contains at least one string
literal.
