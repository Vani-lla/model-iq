import unittest


def strlen(string: str) -> int:
    return len(string)


class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()