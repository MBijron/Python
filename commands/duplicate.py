import shutil
from commands.base.command_base import BaseCommand


class Duplicate(BaseCommand):
    desc = 'Duplicate a file or folder'
    usage = 'DuplicateFile [file/folder] [new name]'
    minArgNr = 2
    maxArgNr = 2
    types = {1: AttributeType.PATH}

    @staticmethod
    def _duplicate_file(path, new) -> None:
        # TODO: write unit test
        shutil.copyfile(path, new)

    @staticmethod
    def _duplicate_folder(path, new) -> None:
        # TODO: write unit test
        shutil.copytree(path, new)

    @staticmethod
    def duplicate_path(path, new) -> None:
        if Duplicate.check_attribute(path, AttributeType.PATH) == AttributeType.FILE:
            Duplicate._duplicate_file(path, new)
        else:
            Duplicate._duplicate_folder(path, new)

    def main(self) -> None:
        # TODO: write unit test
        location = self.__args[1]
        new = self.__args[2]

        self.duplicate_path(location, new)


command = Duplicate(__name__ == "__main__")
