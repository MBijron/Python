import os
import pathlib

from Commands.Base import CommandBase


class ReplaceFilePart(CommandBase.CommandBase):
    args = []
    desc = 'change part of the filename for given replacement'
    usage = 'RenameFilePart.py [filename/directory] [original string] [replacement string]'
    minArgNr = 3
    maxArgNr = 3
    types = {1: CommandBase.AtribType.PATH}
    
    @staticmethod
    def replaceFilePart(location, original, replacement):
        os.rename(location, location.__str__().replace(original, replacement))
    
    @staticmethod
    def replaceFilePartsInPath(location, original, replacement):
        location = pathlib.Path(location)
        if(location.is_file()):
            ReplaceFilePart.replaceFilePart(location, original, replacement)
        elif(location.is_dir()):
            for path, subdirs, files in os.walk(location):
                for name in files:
                    ReplaceFilePart.replaceFilePart(pathlib.PurePath(path, name), original, replacement)
        else:
            raise Exception('The first argument should be a file or directory')

    def main(self):
        location = self.args[1]
        original = self.args[2]
        replacement = self.args[3]
        
        self.replaceFilePartsInPath(location, original, replacement)
          
command = ReplaceFilePart(__name__ == "__main__")