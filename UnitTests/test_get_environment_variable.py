import unittest
import os
from Windows.Environment import Environment


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Environment.expand_variables(Environment.get_environment_variable("path")), os.getenv("path").split(";;")[0])


if __name__ == '__main__':
    unittest.main()
