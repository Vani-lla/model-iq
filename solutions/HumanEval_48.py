import unittest


def is_palindrome(text: str) -> bool:
    return text == text[::-1]


class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_palindrome(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))

if __name__ == '__main__':
    unittest.main()