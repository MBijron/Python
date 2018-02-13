from commands.base import CommandBase, Middleware, CommandParameter
from pyworks.utils import ExtraWorks


class ExtraWorksCommand(CommandBase):
    desc = 'Used to install/update extraworks packages'
    usage = 'extraworks'
    parameters = [
        CommandParameter("action", Middleware.ANY),
        CommandParameter("data", Middleware.ANY)
    ]

    def main(self):
        command = self.get_parameter_value("action")
        data = self.get_parameter_value("data")
        if command == "install":
            print("Installing " + data)
            if not ExtraWorks.requirement_installed(data):
                ExtraWorks.install_requirement(data)
            else:
                print("Package " + data + " was installed already")
        elif command == "reinstall":
            print("Reinstalling " + data)
            ExtraWorks.install_requirement(data)
        else:
            print("Wrong argument given '" + command + "'. Use install or reinstall")


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = ExtraWorksCommand(__name__ == "__main__")
