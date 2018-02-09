# coding=utf-8
from PyWorks.IO import File
import re

class DescriptionInterpreter:
    _description_string = None
    _class_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_";

    def set_file(self, file):
        self._description_string = File.read_text(file)

    def set_text(self, text):
        self._description_string = text;

    def get_components(self):
        print(re.split(r"[\s]+", self._description_string))

    def is_class_name(self, name):
        for character in name:
            if not self.is_class_char(character):
                return False
        return True

    def is_class_char(self, character):
        for allowed_char in self._class_chars:
            if character is allowed_char:
                return True
        return False


interpreter = DescriptionInterpreter()
interpreter.set_file(r"C:\Users\maurice\Dropbox\Documenten\Unified description pattern wiki.txt")
interpreter.get_components();
