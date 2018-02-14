import unittest
from commands.base.command_base import CommandBase
from commands.base.middleware import Middleware
import sys


class TestCommandBase(unittest.TestCase):
    _base_command: CommandBase = None
    _command_arguments: [str] = [
        ".",
        "11-01-2015",
        "foo"
    ]

    def setUp(self) -> None:
        # first, set a few arguments, so the command can behave as expected
        for argument in self._command_arguments:
            sys.argv.append(argument)
            self._base_command = MockCommand(True)


class MockCommand(CommandBase):

    def main(self) -> None:
        pass

class MockCommandWithMiddleware(CommandBase):
    types = {
        1: Middleware.PATH,
        2: Middleware.DATE,
    }

    def main(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
