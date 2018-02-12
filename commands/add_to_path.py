import os
from commands.base import CommandBase, Middleware
from commands.base import AttributeType


class AddToPath(CommandBase):
    desc = 'Add folder to path variable'
    usage = 'AddToPath [path]'
    minArgNr = 1
    maxArgNr = 1
    types = {1: Middleware.PATH}

    @staticmethod
    def _add_folder_to_path(folder):
        # TODO: write unit test
        if not AddToPath._path_already_contains_folder(folder):
            print("folder not in path yet")

    @staticmethod
    def _path_already_contains_folder(folder):
        #TODO: Complete this method, it does not check anything at all!
        path = os.environ["PATH"]
        for pathFolder in path.split(";"):
            print(pathFolder)

    def main(self):
        # TODO: write unit test
        folder = self.__args[1]
        self._add_folder_to_path(folder)


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = AddToPath(__name__ == "__main__")
