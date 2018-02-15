from typing import List

from commands.base.command_base import BaseCommand
from commands.base.middleware import Middleware
from commands.base.command_parameter import CommandParameter
from pyworks.utils.extra_works import ExtraWorks


class ExtraWorksCommand(BaseCommand):
    desc = 'Used to install/update extraworks packages'
    usage = 'extraworks'
    parameters = [
        CommandParameter("action", Middleware.ANY),
        CommandParameter("data", Middleware.ANY)
    ]

    def main(self) -> None:
        action = self.get_parameter_value("action")
        data = self.get_parameter_value("data")
        if action == "install":
            print("Installing " + data)
            if not ExtraWorks.requirement_installed(data):
                ExtraWorks.install_requirement(data)
            else:
                print("Package " + data + " was installed already")
        elif action == "reinstall":
            print("Reinstalling " + data)
            ExtraWorks.install_requirement(data)
        elif action == "uninstall":
            print("Uninstalling " + data)
            if ExtraWorks.requirement_installed(data):
                ExtraWorks.uninstall(data)
            else:
                print("Package is not installed and can't be uninstalled")
        else:
            print("Wrong argument given '" + action + "'. Use install or reinstall")

    def _get_parameters(self) -> List[CommandParameter]:
        return self.parameters


# If the file is called directly (not imported) execute the command.
# If not, create an instance of command, but don't execute it
command = ExtraWorksCommand(__name__ == "__main__")
