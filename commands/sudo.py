import sys
from typing import List

from commands.base.command_base import BaseCommand
from commands.base.command_parameter import CommandParameter
from pyworks.io.path import Path
from pyworks.windows.admin import Admin


class sudoCommand (BaseCommand):
    desc = 'if terminal is not admin, start a new terminal with admin'
    usage = 'sudo'
    parameters = [

    ]

    def main(self) -> None:
        Admin.run_as_admin([sys.executable, Path.combine(Path.get_file_path(__file__), "terminal.py")])

    def _get_parameters(self) -> List[CommandParameter]:
        return self.parameters


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = sudoCommand(__name__ == "__main__")
