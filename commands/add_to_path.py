import os
from commands.base.command_base import BaseCommand
from commands.base.middleware import Middleware


class AddToPath(BaseCommand):
    desc = 'Add folder to path variable'
    usage = 'AddToPath [path]'

    @staticmethod
    def _add_folder_to_path(folder) -> None:
        # TODO: write unit test
        if not AddToPath._path_already_contains_folder(folder):
            print("folder not in path yet")

    @staticmethod
    def _path_already_contains_folder(folder) -> None:
        # TODO: Complete this method, it does not check anything at all!
        path = os.environ["PATH"]
        for pathFolder in path.split(";"):
            print(pathFolder)

    def main(self) -> None:
        # TODO: write unit test
        folder = self.__args[1]
        self._add_folder_to_path(folder)


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = AddToPath(__name__ == "__main__")
