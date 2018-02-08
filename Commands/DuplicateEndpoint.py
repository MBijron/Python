from Commands.ReplaceFilePart import ReplaceFilePart
from Commands.ReplaceTextEndpoint import ReplaceTextEndpoint

from Commands.Base.CommandBase import CommandBase
from Commands.Base.CommandBase import AttributeType
from Commands.Duplicate import Duplicate


class DuplicateEndpoint(CommandBase):
    args = []
    desc = 'Duplicate an endpoint file or folder'
    usage = 'DuplicateEndpointFile [file/folder] [new name] [original name in text] [replacement name in text]'
    minArgNr = 4
    maxArgNr = 4
    types = {1: AttributeType.PATH}

    def main(self):
        # TODO: write unit test
        location = self.args[1]
        new = self.args[2]
        original = self.args[3]
        replacement = self.args[4]

        Duplicate.duplicate_path(location, new)
        ReplaceTextEndpoint.replace_text_in_endpoint_file(new, original, replacement)
        ReplaceFilePart.replace_file_parts_in_path(new, original, replacement)


command = DuplicateEndpoint(__name__ == "__main__")
