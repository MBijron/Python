import unittest

from Windows.Environment import Environment


class MyTestCase(unittest.TestCase):
    def test_something(self):

        varname = "python_test_variable"

        Environment.set_environment_variable(varname, "1")

        # Test if the just created environment variable exists
        self.assertTrue(Environment.environment_variable_exists(varname))

        Environment.delete_environment_variable(varname)


if __name__ == '__main__':
    unittest.main()
