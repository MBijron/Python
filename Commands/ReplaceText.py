import pathlib
from Commands.Base import CommandBase
import pathlib

from Commands.Base import CommandBase


class ReplaceText(CommandBase.CommandBase):
    args = []
    desc = 'convert string in file to another string'
    usage = 'ReplaceTextInFile.py [filename/directory] [original string] [replacement string]'
    minArgNr = 3
    maxArgNr = 3
    types = {1: CommandBase.AtribType.PATH}
    
    @staticmethod
    def replaceTextInFile(location, original, replacement):
        with open(location) as f:
            newText = f.read().replace(original, replacement)
        with open(location, 'w') as f:
            f.write(newText)

    @staticmethod
    def replaceTextInPath(location, original, replacement):
        location = pathlib.Path(location)
        if(location.is_file()):
            ReplaceText.replaceTextInFile(location, original, replacement)
        elif(location.is_dir()):
            for path, subdirs, files in os.walk(location):
                for name in files:
                    ReplaceText.replaceTextInFile(pathlib.PurePath(path, name), original, replacement)
        else:
            raise Exception('The first argument should be a file or directory')

    def main(self):
        location = self.args[1]
        original = self.args[2]
        replacement = self.args[3]
        
        self.replaceTextInPath(location, original, replacement)
          
command = ReplaceText(__name__ == "__main__")