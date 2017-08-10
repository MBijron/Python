from Commands.ReplaceFilePart import ReplaceFilePart
from Commands.ReplaceTextEndpoint import ReplaceTextEndpoint

from Commands.Base import CommandBase
from Commands.Duplicate import Duplicate


class DuplicateEndpoint(CommandBase.CommandBase):
    args = []
    desc = 'Duplicate an endpoint file or folder'
    usage = 'DuplicateEndpointFile [file/folder] [new name] [original name in text] [replacement name in text]'
    minArgNr = 4
    maxArgNr = 4
    types = {1: CommandBase.AtribType.PATH}

    def main(self):
        location = self.args[1]
        new = self.args[2]
        original = self.args[3]
        replacement = self.args[4]

        Duplicate.DuplicatePath(location, new)
        ReplaceTextEndpoint.replaceTextInEndpointFile(new, original, replacement)
        ReplaceFilePart.replaceFilePartsInPath(new, original, replacement)


command = DuplicateEndpoint(__name__ == "__main__")
