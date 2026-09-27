import unittest
from challenge import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_racecar(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_level(self):
        self.assertTrue(is_palindrome("level"))

    def test_hello(self):
        self.assertFalse(is_palindrome("hello"))

    def test_python(self):
        self.assertFalse(is_palindrome("python"))

    def test_single_letter(self):
        self.assertTrue(is_palindrome("a"))

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome("noon"))

    def test_even_length_not_palindrome(self):
        self.assertFalse(is_palindrome("book"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))


if __name__ == "__main__":
    unittest.main()
