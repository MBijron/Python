import shutil

from Commands.Base import CommandBase


class Duplicate(CommandBase.CommandBase):
    desc = 'Duplicate a file or folder'
    usage = 'DuplicateFile [file/folder] [new name]'
    minArgNr = 2
    maxArgNr = 2
    types = {1: CommandBase.AtribType.PATH}

    @staticmethod
    def DuplicateFile(path, new):
        shutil.copyfile(path, new)

    @staticmethod
    def DuplicateFolder(path, new):
        shutil.copytree(path, new)

    @staticmethod
    def DuplicatePath(path, new):
        if (Duplicate.checkAtrib(path, CommandBase.AtribType.PATH) == CommandBase.AtribType.FILE):
            Duplicate.DuplicateFile(path, new)
        else:
            Duplicate.DuplicateFolder(path, new)

    def main(self):
        location = self.args[1]
        new = self.args[2]

        self.DuplicatePath(location, new)


command = Duplicate(__name__ == "__main__")
