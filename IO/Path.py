import shutil
import os
import sys


class Path:
    @staticmethod
    def absolutepath(file):
        # TODO: write unit test
        return os.path.abspath(file)

    @staticmethod
    def workdir():
        # TODO: write unit test
        return os.getcwd()

    @staticmethod
    def scriptpath():
        # TODO: write unit test
        return os.path.dirname(os.path.realpath(sys.argv[0]))

    @staticmethod
    def fromfile(file):
        # TODO: write unit test
        return os.path.dirname(os.path.realpath(file))

    @staticmethod
    def combine(*args):
        # TODO: write unit test
        return os.path.join(*args)
