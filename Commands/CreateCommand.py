from Commands.Base.CommandBase import CommandBase
from IO.File import File
from IO.Path import Path
from Resources.ResourceHandler import ResourceHandler
from Util.Regex import Regex


class CreateCommandCommand (CommandBase):
    desc = 'Create a python command'
    usage = 'CreateCommand [name] [description]'
    minArgNr = 2
    maxArgNr = 2
    types = {}

    def main(self):
        name = self.args[1]
        description = self.args[2]

        if(File.exists(name+'.py')):
            raise Exception('A command with that name already exists')
        File.copy(ResourceHandler.getpath('CommandTemplate'), Path.combine(Path.scriptpath(), name+'.py'))
        Regex.replace_file(Path.combine(Path.scriptpath(), name+'.py'), r"\[NAME\]", name)
        Regex.replace_file(Path.combine(Path.scriptpath(), name+'.py'), r"\[DESCRIPTION\]", description)


command = CreateCommandCommand(__name__ == "__main__")
