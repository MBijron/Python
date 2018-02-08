import unittest
import os

from Windows.Environment import Environment


class MyTestCase(unittest.TestCase):
    def test_environment_variable_exists(self):
        self.assertEqual(Environment.environment_variable_exists("PATH"), True)
        self.assertEqual(Environment.environment_variable_exists("NON_EXISTENT_ENVIRONMENT_VARIABLE_#$(*&Y@#(*"), False)

    def test_expand_variables(self):
        self.assertEqual("something" + Environment.expand_variables("%path%") + "something", "something" + os.getenv("path") + "something")

    def test_get_environment_variable(self):
        #TODO: fix bug where os.getenv("path") includes user variables to path and get_environment_variable does not
        self.maxDiff = None;
        self.assertEqual(Environment.expand_variables(Environment.get_environment_variable("path")), os.getenv("path").split(";;")[0])

    def test_set_environment_variable(self):
        varname = "python_test_variable"
        Environment.set_environment_variable(varname, "1")
        # Test if the just created environment variable exists
        self.assertTrue(Environment.environment_variable_exists(varname))
        Environment.delete_environment_variable(varname)


if __name__ == '__main__':
    unittest.main()
