from Commands.Base.CommandBase import CommandBase
from Commands.Base.CommandBase import AtribType
from Util.Regex import Regex


class RegexCommand(CommandBase):
    args = []
    desc = 'match regex in file or folder'
    usage = 'Regex.py [filename/directory] [pattern] <filer>'
    minArgNr = 2
    maxArgNr = 3
    types = {1: AtribType.PATH}

    def _printresults(self, results):
        for result in results:
            print(result)

    def main(self):
        location = self.args[1]
        pattern = self.args[2]
        if(self.checkAtrib(location, AtribType.PATH) == AtribType.FOLDER):
            if(len(self.args) >= 4):
                print(self._printresults(Regex.match_files(location, pattern, self.args[3])))
            else:
                print(self._printresults(Regex.match_files(location, pattern)))
        else:
            print(Regex.match_file(location, pattern))

command = RegexCommand(__name__ == "__main__")