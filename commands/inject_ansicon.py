from commands.base import CommandBase
from pyworks.io import Path
from pyworks.utils import ExtraWorks
from subprocess import call


class InjectAnsiconCommand(CommandBase):
    desc = 'used to inject ansicon dlls into the current cmd. This makes it possible to use multiple colors in one line'
    usage = 'inject_ansicon'
    minArgNr = 0
    maxArgNr = 0
    types = {}

    def main(self):
        ansicon_path = Path.combine(ExtraWorks.install_if_missing("ansicon@1.60"), "ansicon.exe")
        call([ansicon_path])


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = InjectAnsiconCommand(__name__ == "__main__")
