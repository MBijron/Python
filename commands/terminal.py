from typing import List

from commands.base.command_base import BaseCommand
from commands.base.command_parameter import CommandParameter
from pyworks.utils.extra_works import ExtraWorks
from subprocess import call


class TerminalCommand (BaseCommand):
    desc = 'Start a customized terminal'
    usage = 'terminal'
    parameters = [

    ]

    def main(self) -> None:
        ansicon_path = ExtraWorks.install_if_missing("ansicon@1.81") + "\\ansicon.exe"
        call(["cmd", "/K", ansicon_path, "-p", "&&", "set", "PROMPT=$E[0;36m%username%+ - $P$_$E[36;1m$G$E[0m$S", "&&", "set",  "nl=^&echo.", "&&", "title", "terminal"])

    def _get_parameters(self) -> List[CommandParameter]:
        return self.parameters


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = TerminalCommand(__name__ == "__main__")
