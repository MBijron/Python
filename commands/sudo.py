import sys

from commands.base.command_base import CommandBase
from pyworks.io.path import Path
from pyworks.windows.admin import Admin


class sudoCommand (CommandBase):
    desc = 'if terminal is not admin, start a new terminal with admin'
    usage = 'sudo'
    parameters = [

    ]

    def main(self):
        if not Admin.is_user_admin():
            Admin.run_as_admin([sys.executable, Path.combine(Path.get_file_path(__file__), "terminal.py")])
            sys.exit(1)


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = sudoCommand (__name__ == "__main__")
