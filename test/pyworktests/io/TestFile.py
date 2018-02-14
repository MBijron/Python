import unittest

from pyworks.io.file import File


class MyTestCase(unittest.TestCase):
    def test_readtext(self) -> None:
        self.assertEqual(File.read_text('testResources\\FileTest.txt'), 'Contents Of File\nSecond Line Of Content')

    def test_readlines(self) -> None:
        self.assertEqual(File.read_lines('testResources\\FileTest.txt'), ['Contents Of File\n', 'Second Line Of Content'])

    def test_writetext(self) -> None:
        File.write_text('testResources\\FileTest.txt', "Nothing")
        self.assertEqual(File.read_text('testResources\\FileTest.txt'), "Nothing")
        File.write_text('testResources\\FileTest.txt', 'Contents Of File\nSecond Line Of Content')
        self.assertEqual(File.read_text('testResources\\FileTest.txt'), 'Contents Of File\nSecond Line Of Content')
        pass

    def test_copy(self) -> None:
        File.copy('testResources\\FileTest.txt', "testResources\\FileTestTemp.txt")
        self.assertTrue(File.exists("testResources\\FileTestTemp.txt"))
        File.delete("testResources\\FileTestTemp.txt")
        pass

    def test_exists(self) -> None:
        self.assertTrue(File.exists(r'testResources\FileTest.txt'))
        self.assertFalse(File.exists(r'testResources\FILEDOESNOTEXIST.txt'))

    def test_delete(self) -> None:
        File.copy('testResources\\FileTest.txt', "testResources\\FileTestTemp.txt")
        self.assertTrue(File.exists("testResources\\FileTestTemp.txt"))
        File.delete("testResources\\FileTestTemp.txt")
        self.assertFalse(File.exists("testResources\\FileTestTemp.txt"))
        pass


if __name__ == '__main__':
    unittest.main()
