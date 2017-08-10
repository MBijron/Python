import os
import pathlib
import re
from IO.File import File


class Regex:
    
    @staticmethod
    def match_string(string, pattern):
        regex = re.compile(pattern)
        if regex.search(string):
            return True
        else:
            return False

    @staticmethod
    def match_file(path, pattern):
        text = File.readtext(path)
        return Regex.match_string(text, pattern)

    @staticmethod
    def match_files(path, pattern, filter='.*'):
        matched_files = []
        for location, subdirs, files in os.walk(path):
            for name in files:
                if Regex.match_file(pathlib.PurePath(location, name), pattern) and Regex.match_string(name, filter):
                    matched_files.append(pathlib.PurePath(location, name).__str__())
        return matched_files
