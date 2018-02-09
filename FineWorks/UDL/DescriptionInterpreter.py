# coding=utf-8
from FineWorks.UDL.Tokenizers import SettingTokenizer, ClassTokenizer, ContentsTokenizer
from FineWorks.UDL.Tokens import TokenBase
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
        next_index = 0
        for i in range(0, len(components), 1):
            if i >= next_index:
                token: TokenBase = self.find_token(components, i)
                print(token.get_name())
                next_index = i + token.get_components_used()


    def find_token(self, components: [], index):
        contents_tokenizer = ContentsTokenizer()
        setting_tokenizer = SettingTokenizer()
        class_tokenizer = ClassTokenizer()
        if contents_tokenizer.matches(self.slice_components(components, index, contents_tokenizer.get_requested_component_nr())):
            return contents_tokenizer.get_token()
        if setting_tokenizer.matches(self.slice_components(components, index, setting_tokenizer.get_requested_component_nr())):
            return setting_tokenizer.get_token()
        if class_tokenizer.matches(self.slice_components(components, index, class_tokenizer.get_requested_component_nr())):
            return class_tokenizer.get_token()
        raise Exception("Wrong syntax at: " + (' '.join(components[index: index+7])+"..."))

    def slice_components(self, components: [], index, required_components):
        if required_components < 0:
            return components[index:]
        return components[index:index+required_components]


interpreter = DescriptionInterpreter()
# interpreter.set_file(r"C:\Users\maurice\Dropbox\Documenten\Unified description pattern wiki.txt")
interpreter.set_file(r"C:\Users\mauriceb\Documents\UDLWIKI.txt")
interpreter.create_tokens(interpreter.get_components())
