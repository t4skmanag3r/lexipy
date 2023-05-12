import unittest
from lexipy import Lexer, lexify


class TestLexer(unittest.TestCase):
    def test_basic_lexing(self):
        lexer = Lexer("hello, world!")
        tokens = list(lexer)
        expected_tokens = ["hello", ",", "world", "!"]
        self.assertEqual(tokens, expected_tokens)

    def test_empty_content(self):
        lexer = Lexer("")
        tokens = list(lexer)
        expected_tokens = []
        self.assertEqual(tokens, expected_tokens)

    def test_special_terms(self):
        special_terms = {"[banana]", "[cherry]"}
        lexer = Lexer("apple, [banana], [cherry]", special_terms=special_terms)
        tokens = list(lexer)
        expected_tokens = ["apple", ",", "[banana]", ",", "[cherry]"]
        self.assertEqual(tokens, expected_tokens)

    def test_case_insensitivity(self):
        lexer = Lexer("HELLO, WORLD!")
        tokens = list(lexer)
        expected_tokens = ["hello", ",", "world", "!"]
        self.assertEqual(tokens, expected_tokens)

    def test_numeric_tokens(self):
        lexer = Lexer("123, 456, 789")
        tokens = list(lexer)
        expected_tokens = ["123", ",", "456", ",", "789"]
        self.assertEqual(tokens, expected_tokens)

    def test_alphanumeric_tokens(self):
        lexer = Lexer("abc123, def456, ghi789")
        tokens = list(lexer)
        expected_tokens = ["abc123", ",", "def456", ",", "ghi789"]
        self.assertEqual(tokens, expected_tokens)

    def test_whitespace_handling(self):
        lexer = Lexer("   Hello,   World!   ")
        tokens = list(lexer)
        expected_tokens = ["hello", ",", "world", "!"]
        self.assertEqual(tokens, expected_tokens)

    def test_lexify(self):
        tokens = lexify("Hello, World!")
        excepted_tokens = ["hello", ",", "world", "!"]
        self.assertEqual(tokens, excepted_tokens)
