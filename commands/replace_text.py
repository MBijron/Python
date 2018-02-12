import pathlib
import os

from commands.base.command_base import CommandBase
from commands.base.attribute_type import AttributeType


class ReplaceText(CommandBase):
    __args = []
    desc = 'convert string in file to another string'
    usage = 'ReplaceTextInFile.py [filename/directory] [original string] [replacement string]'
    minArgNr = 3
    maxArgNr = 3
    types = {1: AttributeType.PATH}

    @staticmethod
    def _replace_text_in_file(location, original, replacement):
        # TODO: write unit test
        with open(location) as f:
            new_text = f.read().replace(original, replacement)
        with open(location, 'w') as f:
            f.write(new_text)

    @staticmethod
    def replace_text_in_path(location, original, replacement):
        # TODO: write unit test
        location = pathlib.Path(location)
        if location.is_file():
            ReplaceText._replace_text_in_file(location, original, replacement)
        elif location.is_dir():
            # noinspection PyTypeChecker
            for path, sub_dirs, files in os.walk(location):
                for name in files:
                    ReplaceText._replace_text_in_file(pathlib.PurePath(path, name), original, replacement)
        else:
            raise Exception('The first argument should be a file or directory')

    def main(self):
        # TODO: write unit test
        location = self.args[1]
        original = self.args[2]
        replacement = self.args[3]

        self.replace_text_in_path(location, original, replacement)


command = ReplaceText(__name__ == "__main__")
