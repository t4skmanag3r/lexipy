# LexiPy

LexiPy is a Python package that provides a simple lexer implementation. It allows you to tokenize a string by breaking it down into individual tokens. LexiPy also supports the usage of special terms, which can be treated as one token during tokenization, this can be usefull in domain specific cases like programming languages.

## Installation

You can install LexiPy using pip:

```shell
pip install lexipy
```

## Usage

### Lexer Class (iterator)

The `Lexer` class returns an iterator over the tokens

```python
from lexipy import Lexer

content = "Hello, World!"
lexer = Lexer(content, special_terms=None) # Iterator
tokens = list(lexer) # list of tokens list[str]

tokens
>>> ['hello', ',', 'world', '!']
```

- `content` (str): The string to be tokenized.
- `special_terms` (set[str] | None, optional): A set of special terms to be treated as one token. Default is `None`.

Returns an iterator over the tokens

### lexify Function

The `lexify` function provides a more convenient way to tokenize a string.

```python
from lexipy import lexify

content = "Hello, World!"
tokens = lexify(content, special_terms=None)

tokens
>>> ['hello', ',', 'world', '!']
```

- `content` (str): The string to be tokenized.
- `special_terms` (set[str] | None, optional): A set of special terms to be treated as one token. Default is `None`.

Returns a list of tokens.

### Special terms

You can specify a set of special terms that should be treated as one token during the tokenization process. This can be useful when tokenizing programming languages or other cases where certain terms should not be split.

```python
from lexipy import Lexer

content = "Hello, World!"
special_terms = {"world!"}
lexer = Lexer(content, special_terms=special_terms)
tokens = list(lexer)

tokens
>>> ['hello', ',', 'world!']
```

Note: The special terms are case insensitive

### Planed features

- Adding an optional word stemmer (default: nltk), also support for custom stemmers through an interface

## Contributing

Contributions to LexiPy are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/t4skmanag3r/lexipy).

## License

LexiPy is licensed under the [MIT License](https://opensource.org/licenses/mit).

## References

- [Github Repository](https://github.com/t4skmanag3r/lexipy)
- [PyPI package](https://pypi.org/project/lexipy/)
