import os
import shutil


class Directory:
    @staticmethod
    def exists(directory):
        return os.path.isdir(directory)

    @staticmethod
    def delete(directory):
        shutil.rmtree(directory)
