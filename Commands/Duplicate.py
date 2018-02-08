import shutil

from Commands.Base.CommandBase import CommandBase
from Commands.Base.CommandBase import AttributeType


class Duplicate(CommandBase):
    desc = 'Duplicate a file or folder'
    usage = 'DuplicateFile [file/folder] [new name]'
    minArgNr = 2
    maxArgNr = 2
    types = {1: AttributeType.PATH}

    @staticmethod
    def _duplicate_file(path, new):
        # TODO: write unit test
        shutil.copyfile(path, new)

    @staticmethod
    def _duplicate_folder(path, new):
        # TODO: write unit test
        shutil.copytree(path, new)

    @staticmethod
    def duplicate_path(path, new):
        if Duplicate.check_attribute(path, AttributeType.PATH) == AttributeType.FILE:
            Duplicate._duplicate_file(path, new)
        else:
            Duplicate._duplicate_folder(path, new)

    def main(self):
        # TODO: write unit test
        location = self.args[1]
        new = self.args[2]

        self.duplicate_path(location, new)


command = Duplicate(__name__ == "__main__")
