import shutil
import os
import sys

class File:
    @staticmethod
    def readtext(path):
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.read()

    @staticmethod
    def readlines(path):
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.readlines()

    @staticmethod
    def writetext(path, text):
        with open(path, 'w') as file:
            file.write(text);

    @staticmethod
    def copy(source, dest):
        shutil.copyfile(source, dest)

    @staticmethod
    def exists(file):
        return os.path.isfile(file)

    @staticmethod
    def delete(file):
        os.remove(file)