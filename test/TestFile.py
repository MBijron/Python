import unittest

from IO.File import File


class MyTestCase(unittest.TestCase):
    def test_readtext(self):
        self.assertEqual(File.readtext('testResources\\FileTest.txt'), 'Contents Of File\nSecond Line Of Content')

    def test_readlines(self):
        self.assertEqual(File.readlines('testResources\\FileTest.txt'), [ 'Contents Of File\n', 'Second Line Of Content' ])

    def test_writetext(self):
        File.writetext('testResources\\FileTest.txt', "Nothing");
        self.assertEqual(File.readtext('testResources\\FileTest.txt'), "Nothing")
        File.writetext('testResources\\FileTest.txt', 'Contents Of File\nSecond Line Of Content');
        self.assertEqual(File.readtext('testResources\\FileTest.txt'), 'Contents Of File\nSecond Line Of Content')
        pass

    def test_copy(self):
        File.copy('testResources\\FileTest.txt', "testResources\\FileTestTemp.txt")
        self.assertTrue(File.exists("testResources\\FileTestTemp.txt"))
        File.delete("testResources\\FileTestTemp.txt")
        pass

    def test_exists(self):
        self.assertTrue(File.exists(r'testResources\FileTest.txt'))
        self.assertFalse(File.exists(r'testResources\FILEDOESNOTEXIST.txt'))

    def test_delete(self):
        File.copy('testResources\\FileTest.txt', "testResources\\FileTestTemp.txt")
        self.assertTrue(File.exists("testResources\\FileTestTemp.txt"))
        File.delete("testResources\\FileTestTemp.txt")
        self.assertFalse(File.exists("testResources\\FileTestTemp.txt"))
        pass


if __name__ == '__main__':
    unittest.main()
