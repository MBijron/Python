from Commands.Base.CommandBase import CommandBase
from Commands.Base.CommandBase import AttributeType
from Util.Regex import Regex


class RegexCommand(CommandBase):
    desc = 'match regex in file or folder'
    usage = 'Regex.py [filename/directory] [pattern] <filer>'
    minArgNr = 2
    maxArgNr = 3
    types = {1: AttributeType.PATH}

    @staticmethod
    def _print_results(results):
        for result in results:
            print(result)

    def main(self):
        # TODO: write unit test
        location = self.args[1]
        pattern = self.args[2]
        if self.check_attribute(location, AttributeType.PATH) == AttributeType.FOLDER:
            if len(self.args) >= 4:
                print(self._print_results(Regex.match_files(location, pattern, self.args[3])))
            else:
                print(self._print_results(Regex.match_files(location, pattern)))
        else:
            print(Regex.match_file(location, pattern))


command = RegexCommand(__name__ == "__main__")
