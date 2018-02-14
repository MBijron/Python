from commands.base.command_base import CommandBase
from pyworks.utils.regex import Regex


class RegexCommand(CommandBase):
    desc = 'match regex in file or folder'
    usage = 'regex.py [filename/directory] [pattern] <filer>'
    minArgNr = 2
    maxArgNr = 3
    types = {1: AttributeType.PATH}

    @staticmethod
    def _print_results(results) -> None:
        for result in results:
            print(result)

    def main(self) -> None:
        # TODO: write unit test
        location = self.__args[1]
        pattern = self.__args[2]
        if self.check_attribute(location, AttributeType.PATH) == AttributeType.FOLDER:
            if len(self.__args) >= 4:
                print(self._print_results(Regex.match_files(location, pattern, self.__args[3])))
            else:
                print(self._print_results(Regex.match_files(location, pattern)))
        else:
            print(Regex.match_file(location, pattern))


command = RegexCommand(__name__ == "__main__")
