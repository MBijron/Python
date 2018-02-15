import os
import pathlib
from commands.base.command_base import BaseCommand


class ReplaceFilePart(BaseCommand):
    __args = []
    desc = 'change part of the filename for given replacement'
    usage = 'RenameFilePart.py [filename/directory] [original string] [replacement string]'
    minArgNr = 3
    maxArgNr = 3
    types = {1: AttributeType.PATH}

    @staticmethod
    def _replace_file_part(location, original, replacement) -> None:
        # TODO: write unit test
        os.rename(location, location.__str__().replace(original, replacement))

    @staticmethod
    def replace_file_parts_in_path(location, original, replacement) -> None:
        # TODO: write unit test
        location = pathlib.Path(location)
        if location.is_file():
            ReplaceFilePart._replace_file_part(location, original, replacement)
        elif location.is_dir():
            # noinspection PyTypeChecker
            for path, sub_dirs, files in os.walk(location):
                for name in files:
                    ReplaceFilePart._replace_file_part(pathlib.PurePath(path, name), original, replacement)
        else:
            raise Exception('The first argument should be a file or directory')

    def main(self) -> None:
        # TODO: write unit test
        location = self.args[1]
        original = self.args[2]
        replacement = self.args[3]

        self.replace_file_parts_in_path(location, original, replacement)


command = ReplaceFilePart(__name__ == "__main__")
