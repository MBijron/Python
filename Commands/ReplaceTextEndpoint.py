from Commands import ReplaceText
from Commands.Base import CommandBase


class ReplaceTextEndpoint(CommandBase.CommandBase):
    args = []
    desc = 'convert string in endpoint file to another string'
    usage = 'ReplaceTextInEndpointFile.py [filename/directory] [original string] [replacement string]'
    minArgNr = 3
    maxArgNr = 3
    types = {1: CommandBase.AtribType.PATH}
    
    @staticmethod
    def replaceTextInEndpointFile(location, original, replacement):
        # TODO: write unit test
        command = ReplaceText.ReplaceText(False)
        command.replaceTextInPath(location, original, replacement)
        original = original[0].lower() + original[1:]
        replacement = replacement[0].lower() + replacement[1:]
        command.replaceTextInPath(location, original, replacement)

    def main(self):
        # TODO: write unit test
        location = self.args[1]
        original = self.args[2]
        replacement = self.args[3]
        
        self.replaceTextInEndpointFile(location, original, replacement)
          
command = ReplaceTextEndpoint(__name__ == "__main__")