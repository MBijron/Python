import unittest
from commands.base import CommandBase, Middleware
import sys


class TestCommandBase(unittest.TestCase):
    _base_command: CommandBase = None
    _command_arguments: [str] = [
        ".",
        "11-01-2015",
        "foo"
    ]

    def setUp(self):
        # first, set a few arguments, so the command can behave as expected
        for argument in self._command_arguments:
            sys.argv.append(argument)
            self._base_command = MockCommand(True)

    def test_get_argument__returns_correct_arguments(self):

        for idx, value in enumerate(self._command_arguments):
            self.assertEqual(value, self._base_command._get_argument(idx + 1))

    def test_get_argument__throws_out_of_range_exception(self):
        self.assertRaises(Exception, lambda: self._base_command._get_argument(4))

    def test_add_middleware__checks_correctly(self):
        self._base_command = MockCommand(True)


class MockCommand(CommandBase):

    def main(self):
        pass

class MockCommandWithMiddleware(CommandBase):
    types = {
        1: Middleware.PATH,
        2: Middleware.DATE,
    }

    def main(self):
        pass


if __name__ == '__main__':
    unittest.main()
