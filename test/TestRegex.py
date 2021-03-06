import unittest

from Util.Regex import Regex


class MyTestCase(unittest.TestCase):
    def test_match_string(self):
        self.assertTrue(Regex.match_string("dit is een tekst", "[is]{2}\s*\w+"))
        self.assertFalse(Regex.match_string("dit is een tekst", "^[is]{2}\s*\w+$"))

    def test_match_file(self):
        self.assertTrue(Regex.match_file("TestRegex.py", "[is]{2}\s*\w+"))
        self.assertFalse(Regex.match_file("TestRegex.py", "^[is]{2}\s*\w+$"))

    def test_match_files(self):
        self.assertEqual(Regex.match_files("TestResources", "[is]{2}\s*\w+"), ['TestResources\\RegexMatchTest.txt'])

    def test_replace_string(self):
        self.assertEqual(Regex.replace_string("dit is een tekst", "[is]{2}\s*\w+", "is geen"), "dit is geen tekst")

    def test_replace_file(self):
        Regex.replace_file('TestResources\\RegexMatchTest.txt', "[is]{2}\s*\w+", "is geen")
        self.assertTrue(Regex.match_file('TestResources\\RegexMatchTest.txt', "is geen"))
        Regex.replace_file("TestResources\\RegexMatchTest.txt", "[is]{2}\s*\w+", "is een")
        self.assertTrue(Regex.match_file('TestResources\\RegexMatchTest.txt', "is een"))

    def test_replace_files(self):
        Regex.replace_files('TestResources', "[is]{2}\s*\w+", "is geen")
        self.assertTrue(Regex.match_file('TestResources\\RegexMatchTest.txt', "is geen"))
        Regex.replace_files("TestResources", "[is]{2}\s*\w+", "is een")
        self.assertTrue(Regex.match_file('TestResources\\RegexMatchTest.txt', "is een"))

    def test_replace_files_with_filter(self):
        Regex.replace_files('TestResources', "[is]{2}\s*\w+", "is geen", "cant_match_anything")
        self.assertFalse(Regex.match_file('TestResources\\RegexMatchTest.txt', "is geen"))


if __name__ == '__main__':
    unittest.main()
