import unittest
from Windows.Environment import Environment


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Environment.environment_variable_exists("PATH"), True)
        self.assertEqual(Environment.environment_variable_exists("NON_EXISTENT_ENVIRONMENT_VARIABLE_#$(*&Y@#(*"), False)



if __name__ == '__main__':
    unittest.main()
