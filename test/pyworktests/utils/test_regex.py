import unittest

from pyworks.utils.regex import Regex


class MyTestCase(unittest.TestCase):
    def test_match_string(self) -> None:
        self.assertTrue(Regex.match_string("dit is een tekst", "[is]{2}\s*\w+"))
        self.assertFalse(Regex.match_string("dit is een tekst", "^[is]{2}\s*\w+$"))

    def test_match_file(self) -> None:
        self.assertTrue(Regex.match_file(r".\pyworktests\utils\test_regex.py", "[is]{2}\s*\w+"))
        self.assertFalse(Regex.match_file(r".\pyworktests\utils\test_regex.py", "^[is]{2}\s*\w+$"))

    def test_match_files(self) -> None:
        self.assertEqual(Regex.match_files("testresources", "[is]{2}\s*\w+"), ['testresources\\RegexMatchTest.txt'])

    def test_replace_string(self) -> None:
        self.assertEqual(Regex.replace_string("dit is een tekst", "[is]{2}\s*\w+", "is geen"), "dit is geen tekst")

    def test_replace_file(self) -> None:
        Regex.replace_file('testresources\\RegexMatchTest.txt', "[is]{2}\s*\w+", "is geen")
        self.assertTrue(Regex.match_file('testresources\\RegexMatchTest.txt', "is geen"))
        Regex.replace_file("testresources\\RegexMatchTest.txt", "[is]{2}\s*\w+", "is een")
        self.assertTrue(Regex.match_file('testresources\\RegexMatchTest.txt', "is een"))

    def test_replace_files(self) -> None:
        Regex.replace_files('testresources', "[is]{2}\s*\w+", "is geen")
        self.assertTrue(Regex.match_file('testresources\\RegexMatchTest.txt', "is geen"))
        Regex.replace_files("testresources", "[is]{2}\s*\w+", "is een")
        self.assertTrue(Regex.match_file('testresources\\RegexMatchTest.txt', "is een"))

    def test_replace_files_with_filter(self) -> None:
        Regex.replace_files('testresources', "[is]{2}\s*\w+", "is geen", "cant_match_anything")
        self.assertFalse(Regex.match_file('testresources\\RegexMatchTest.txt', "is geen"))


if __name__ == '__main__':
    unittest.main()
