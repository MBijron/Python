import os
import shutil


class Directory:
    @staticmethod
    def exists(directory) -> bool:
        return os.path.isdir(directory)

    @staticmethod
    def delete(directory) -> None:
        shutil.rmtree(directory)
