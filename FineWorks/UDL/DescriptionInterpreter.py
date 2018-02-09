# coding=utf-8
from PyWorks.IO import File
import re

class DescriptionInterpreter:
    _description_string = None
    _split_regex = r"[\s]+"

    def set_file(self, file):
        self._description_string = File.read_text(file)

    def set_text(self, text):
        self._description_string = text;

    def get_components(self):
        return re.split(self._split_regex, self._description_string)

    def create_tokens(self, components):
        pass


interpreter = DescriptionInterpreter()
# interpreter.set_file(r"C:\Users\maurice\Dropbox\Documenten\Unified description pattern wiki.txt")
interpreter.set_file(r"C:\Users\mauriceb\Documents\UDLWIKI.txt")
interpreter.get_components()
