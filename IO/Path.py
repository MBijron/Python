import shutil
import os
import sys


class Path:
    @staticmethod
    def get_absolute_path(file):
        # TODO: write unit test
        return os.path.abspath(file)

    @staticmethod
    def get_working_directory():
        # TODO: write unit test
        return os.getcwd()

    @staticmethod
    def get_script_path():
        # TODO: write unit test
        return os.path.dirname(os.path.realpath(sys.argv[0]))

    @staticmethod
    def get_file_path(file):
        # TODO: write unit test
        return os.path.dirname(os.path.realpath(file))

    @staticmethod
    def combine(*args):
        # TODO: write unit test
        return os.path.join(*args)
