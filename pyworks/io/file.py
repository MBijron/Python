import os
import shutil
from typing import List


class File:
    @staticmethod
    def read_text(path) -> str:
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.read()

    @staticmethod
    def read_lines(path) -> List[str]:
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.readlines()

    @staticmethod
    def write_text(path, text) -> None:
        with open(path, 'w') as file:
            file.write(text)

    @staticmethod
    def copy(source, destination) -> None:
        shutil.copyfile(source, destination)

    @staticmethod
    def exists(file) -> bool:
        return os.path.isfile(file)

    @staticmethod
    def delete(file) -> None:
        os.remove(file)
