from commands import replace_text
from commands.base.command_base import CommandBase


class ReplaceTextEndpoint(CommandBase):
    desc = 'convert string in endpoint file to another string'
    usage = 'ReplaceTextInEndpointFile.py [filename/directory] [original string] [replacement string]'
    minArgNr = 3
    maxArgNr = 3
    types = {1: AttributeType.PATH}

    @staticmethod
    def replace_text_in_endpoint_file(location, original, replacement):
        # TODO: write unit test
        cmd = replace_text.ReplaceText(False)
        cmd.replace_text_in_path(location, original, replacement)
        original = original[0].lower() + original[1:]
        replacement = replacement[0].lower() + replacement[1:]
        cmd.replace_text_in_path(location, original, replacement)

    def main(self):
        # TODO: write unit test
        location = self.__args[1]
        original = self.__args[2]
        replacement = self.__args[3]

        self.replace_text_in_endpoint_file(location, original, replacement)


command = ReplaceTextEndpoint(__name__ == "__main__")
