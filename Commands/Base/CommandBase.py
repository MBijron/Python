import sys
import pathlib
from enum import Enum


class CommandBase:
    args = []
    desc = 'No description available for this command'
    usage = 'No useage available for this command'
    minArgNr = None
    maxArgNr = None
    types = {}

    def main(self):
        raise Exception('The commands main function is not implemented')

    @staticmethod
    def checkAtrib(atrib, type):
        path = pathlib.Path(atrib)
        if (type == AtribType.FILE):
            if (path.is_file):
                return type
            else:
                raise Exception('The attirbute should be a file')
        elif (type == AtribType.FOLDER):
            if (path.is_dir()):
                return type
            else:
                raise Exception('The attribute should be a folder')
        elif (type == AtribType.PATH):
            if path.is_file():
                return AtribType.FILE
            elif (path.is_dir()):
                return AtribType.FOLDER
            else:
                raise Exception('The attribute should be a file or folder')
        else:
            raise Exception('The type to validate is not supported')

    def checkTypes(self):
        for key, value in self.types.items():
            self.checkAtrib(self.args[key], value)

    def run(self, args):
        self.args = args
        if ((self.minArgNr != None and len(self.args) < self.minArgNr + 1) or (
                self.maxArgNr != None and len(self.args) > self.maxArgNr + 1)):
            raise Exception('Wrong number of arguments given\n' + 'usage: ' + self.usage)
        if (len(self.args) >= 2 and self.args[1] == "/help"):
            print(self.desc)
            print('usage: ' + self.usage)
            sys.exit(1)
        if (len(self.types) > 0):
            self.checkTypes()
        self.main()

    def __init__(self, run):
        if (run):
            self.run(sys.argv)


class AtribType(Enum):
    FILE = 1
    FOLDER = 2
    PATH = 3
