from typing import List
from commands.base.command_parameter import CommandParameter
from commands.base.middleware import Middleware
from commands.base.command_base import BaseCommand
from pyworks.io.file import File
from pyworks.io.path import Path
from pyworks.resources.resource_handler import ResourceHandler
from pyworks.utils.regex import Regex


class CreateCommandCommand (BaseCommand):
    desc = 'Create a python command'
    usage = 'CreateCommand [name] [description]'
    parameters = [
        CommandParameter("name", Middleware.ANY),
        CommandParameter("description", Middleware.ANY)
    ]

    def main(self) -> None:
        # TODO: write unit test
        name = self.get_parameter_value("name")
        description = self.get_parameter_value("description")

        if File.exists(name + '.py'):
            raise Exception('A command with that name already exists')
        File.copy(ResourceHandler.get_resource_path('command_template'), Path.combine(Path.get_script_path(), name + '.py'))
        Regex.replace_file(Path.combine(Path.get_script_path(), name + '.py'), r"\[NAME\]", name)
        Regex.replace_file(Path.combine(Path.get_script_path(), name + '.py'), r"\[DESCRIPTION\]", description)

    def _get_parameters(self) -> List[CommandParameter]:
        return self.parameters


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = CreateCommandCommand(__name__ == "__main__")
