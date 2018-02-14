from commands.base.command_base import CommandBase
from pyworks.utils.extra_works import ExtraWorks
from subprocess import call


class TerminalCommand (CommandBase):
    desc = 'Start a customized terminal'
    usage = 'terminal'
    minArgNr = 0
    maxArgNr = 0
    types = {}

    def main(self) -> None:
        ansicon_path = ExtraWorks.install_if_missing("ansicon@1.81") + "\\ansicon.exe"
        call(["cmd", "/K", ansicon_path, "-p", "&&", "set", "PROMPT=$E[0;36m%username%+ - $P$_$E[36;1m$G$E[0m$S", "&&", "set",  "nl=^&echo.", "&&", "title", "terminal"])


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = TerminalCommand (__name__ == "__main__")
