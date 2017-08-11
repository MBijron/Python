import os
import pathlib
import re
from IO.File import File

class Regex:

    @staticmethod
    def match_string(string, pattern):
        # TODO: write unit test
        regex = re.compile(pattern)
        if regex.search(string):
            return True
        else:
            return False

    @staticmethod
    def match_file(path, pattern):
        # TODO: write unit test
        text = File.readtext(path)
        return Regex.match_string(text, pattern)

    @staticmethod
    def match_files(path, pattern, filter='.*'):
        # TODO: write unit test
        matched_files = []
        for location, subdirs, files in os.walk(path):
            for name in files:
                if Regex.match_string(name, filter) and Regex.match_file(pathlib.PurePath(location, name), pattern):
                    matched_files.append(pathlib.PurePath(location, name).__str__())
        return matched_files

    @staticmethod
    def replace_string(string, pattern, replacement):
        # TODO: write unit test
        return re.sub(pattern, replacement, string)

    @staticmethod
    def replace_file(path, pattern, replacement):
        # TODO: write unit test
        text = File.readtext(path)
        text = Regex.replace_string(text, pattern, replacement)
        File.writetext(path, text)

    @staticmethod
    def replace_files(path, pattern, filter='.*'):
        # TODO: write unit test
        for location, subdirs, files in os.walk(path):
            for name in files:
                if Regex.match_string(name, filter):
                    Regex.replace_file(pathlib.PurePath(location, name), pattern)
