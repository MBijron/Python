import pathlib
import sys
from enum import Enum
from Util.DateTimeUtil import DateTimeUtil


class CommandBase:
    args = []
    desc = 'No description available for this command'
    usage = 'No Usage available for this command'
    minArgNr = None
    maxArgNr = None
    types = {}

    def main(self):
        raise Exception('The commands main function is not implemented')

    @staticmethod
    def check_attribute(attribute, type):
        path = pathlib.Path(attribute)
        if type == AttributeType.FILE:
            if path.is_file:
                return type
            else:
                raise Exception('The attribute should be a file')
        elif type == AttributeType.FOLDER:
            if path.is_dir():
                return type
            else:
                raise Exception('The attribute should be a folder')
        elif type == AttributeType.PATH:
            if path.is_file():
                return AttributeType.FILE
            elif path.is_dir():
                return AttributeType.FOLDER
            else:
                raise Exception('The attribute should be a file or folder')
        elif type == AttributeType.DATE:
            if DateTimeUtil.is_date(attribute):
                return type
            else:
                raise Exception('The attribute should be a date')
        else:
            raise Exception('The type to validate is not supported')

    def _check_types(self):
        for key, value in self.types.items():
            try:
                self.check_attribute(self.args[key], value)
            except Exception as e:
                raise Exception('Attribute "' + self.args[key] + '" is of a wrong type: ' + str(e))

    def run(self, args):
        self.args = args
        if len(self.args) >= 2 and self.args[1] == "/help":
            print(self.desc)
            print('usage: ' + self.usage)
            sys.exit(1)
        if ((self.minArgNr is not None and len(self.args) < self.minArgNr + 1) or (
                self.maxArgNr is not None and len(self.args) > self.maxArgNr + 1)):
            raise Exception('Wrong number of arguments given\n' + 'usage: ' + self.usage)
        if len(self.types) > 0:
            self._check_types()
        self.main()

    def __init__(self, run):
        if run:
            self.run(sys.argv)


class AttributeType(Enum):
    FILE = 1
    FOLDER = 2
    PATH = 3
    DATE = 4
