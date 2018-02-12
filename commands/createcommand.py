from commands.base.command_base import CommandBase
from pyworks.io import File
from pyworks.io.path import Path
from pyworks.resources.resource_handler import ResourceHandler
from pyworks.utils.regex import Regex


class CreateCommandCommand (CommandBase):
    desc = 'Create a python command'
    usage = 'CreateCommand [name] [description]'
    minArgNr = 2
    maxArgNr = 2
    types = {}

    def main(self):
        # TODO: write unit test
        name = self.__args[1]
        description = self.__args[2]

        if File.exists(name + '.py'):
            raise Exception('A command with that name already exists')
        File.copy(ResourceHandler.get_resource_path('command_template'), Path.combine(Path.get_script_path(), name + '.py'))
        Regex.replace_file(Path.combine(Path.get_script_path(), name + '.py'), r"\[NAME\]", name)
        Regex.replace_file(Path.combine(Path.get_script_path(), name + '.py'), r"\[DESCRIPTION\]", description)


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = CreateCommandCommand(__name__ == "__main__")
