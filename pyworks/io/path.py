import os
import sys


class Path:
    @staticmethod
    def get_absolute_path(file) -> str:
        # TODO: write unit test
        return os.path.abspath(file)

    @staticmethod
    def get_working_directory() -> str:
        # TODO: write unit test
        return os.getcwd()

    @staticmethod
    def get_script_path() -> str:
        # TODO: write unit test
        return os.path.dirname(os.path.realpath(sys.argv[0]))

    @staticmethod
    def get_file_path(file) -> str:
        # TODO: write unit test
        return os.path.dirname(os.path.realpath(file))

    @staticmethod
    def combine(*args) -> str:
        # TODO: write unit test
        return os.path.join(*args)
