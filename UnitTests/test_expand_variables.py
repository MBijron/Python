import unittest
import os

from Windows.Environment import Environment


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("something" + Environment.expand_variables("%path%") + "something", "something" + os.getenv("path") + "something")


if __name__ == '__main__':
    unittest.main()
