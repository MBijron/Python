import shutil
import os
import sys

class File:
    @staticmethod
    def readtext(path):
        # TODO: write unit test
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.read()

    @staticmethod
    def readlines(path):
        # TODO: write unit test
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.readlines()

    @staticmethod
    def writetext(path, text):
        # TODO: write unit test
        with open(path, 'w') as file:
            file.write(text);

    @staticmethod
    def copy(source, dest):
        # TODO: write unit test
        shutil.copyfile(source, dest)

    @staticmethod
    def exists(file):
        # TODO: write unit test
        return os.path.isfile(file)