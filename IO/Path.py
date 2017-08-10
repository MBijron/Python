import shutil
import os
import sys


class Path:
    @staticmethod
    def absolutepath(file):
        return os.path.abspath(file)

    @staticmethod
    def workdir():
        return os.getcwd()

    @staticmethod
    def scriptpath():
        return os.path.dirname(os.path.realpath(sys.argv[0]))

    @staticmethod
    def fromfile(file):
        return os.path.dirname(os.path.realpath(file))

    @staticmethod
    def combine(*args):
        return os.path.join(*args)
