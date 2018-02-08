import pathlib
import inspect
import sys

from Commands.Base.AttributeType import AttributeType
from Util.DateTimeUtil import DateTimeUtil
from Commands.Middleware.MiddlewareBase import MiddlewareBase


class CommandBase:
    __args = []
    desc = 'No description available for this command'
    usage = 'No Usage available for this command'
    minArgNr = None
    maxArgNr = None
    types = {}

    def main(self):
        raise NotImplementedError

    @staticmethod
    def check_attribute(attribute, middleware : MiddlewareBase):
        try:
            middleware.check(attribute)
        except Exception as e:
            raise e

        path = pathlib.Path(attribute)
        elif middleware == AttributeType.FOLDER:
            if path.is_dir():
                return middleware
            else:
                raise Exception('The attribute should be a folder')
        elif middleware == AttributeType.PATH:
            if path.is_file():
                return AttributeType.FILE
            elif path.is_dir():
                return AttributeType.FOLDER
            else:
                raise Exception('The attribute should be a file or folder')

    def __check_types(self):
        for arg_index, middleware in self.types.items():
            if inspect.isclass(MiddlewareBase):
                try:
                    self.check_attribute(self.__args[arg_index], middleware)
                except Exception as e:
                    raise Exception('Attribute "' + self.__args[arg_index] + '" is of a wrong type: ' + str(e))
            else:
                raise Exception('The middleware for attribute "' + self.__args[arg_index] + '" is not of type MiddlewareBase')

    def __run(self, args):
        self.__args = args
        if len(self.__args) >= 2 and self.__args[1] == "/help":
            print(self.desc)
            print('usage: ' + self.usage)
            sys.exit(1)
        if ((self.minArgNr is not None and len(self.__args) < self.minArgNr + 1) or (
                self.maxArgNr is not None and len(self.__args) > self.maxArgNr + 1)):
            raise Exception('Wrong number of arguments given\n' + 'usage: ' + self.usage)
        if len(self.types) > 0:
            self.__check_types()
        self.main()

    def __init__(self, run):
        if run:
            self.__run(sys.argv)
