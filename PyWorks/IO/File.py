import os
import shutil


class File:
    @staticmethod
    def read_text(path):
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.read()

    @staticmethod
    def read_lines(path):
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.readlines()

    @staticmethod
    def write_text(path, text):
        with open(path, 'w') as file:
            file.write(text)

    @staticmethod
    def copy(source, destination):
        shutil.copyfile(source, destination)

    @staticmethod
    def exists(file):
        return os.path.isfile(file)

    @staticmethod
    def delete(file):
        os.remove(file)
