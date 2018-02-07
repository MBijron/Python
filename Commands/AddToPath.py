import shutil
import os

from Commands.Base import CommandBase


class AddToPath(CommandBase.CommandBase):
    desc = 'Add folder to path variable'
    usage = 'AddToPath [path]'
    minArgNr = 1
    maxArgNr = 1
    types = {1: CommandBase.AtribType.PATH}

    @staticmethod
    def AddFolderToPath(folder):
        # TODO: write unit test
        if not AddToPath.PathAlreadyContainsFolder(folder):
            print("folder not in path yet")

    @staticmethod
    def PathAlreadyContainsFolder(folder):
        path = os.environ["PATH"]
        for pathFolder in path.split(";"):
            print(pathFolder)


    def main(self):
        # TODO: write unit test
        folder = self.args[1]
        self.AddFolderToPath(folder)


command = AddToPath(__name__ == "__main__")
