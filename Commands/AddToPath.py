import os
from Commands.Base.CommandBase import CommandBase
from Commands.Base.CommandBase import AttributeType


class AddToPath(CommandBase):
    desc = 'Add folder to path variable'
    usage = 'AddToPath [path]'
    minArgNr = 1
    maxArgNr = 1
    types = {1: AttributeType.PATH}

    @staticmethod
    def _add_folder_to_path(folder):
        # TODO: write unit test
        if not AddToPath._path_already_contains_folder(folder):
            print("folder not in path yet")

    @staticmethod
    def _path_already_contains_folder(folder):
        path = os.environ["PATH"]
        for pathFolder in path.split(";"):
            print(pathFolder)

    def main(self):
        # TODO: write unit test
        folder = self.args[1]
        self._add_folder_to_path(folder)


command = AddToPath(__name__ == "__main__")
