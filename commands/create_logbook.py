from typing import List

from commands.base.command_parameter import CommandParameter
from commands.base.middleware import Middleware
from commands.base.command_base import BaseCommand


class CreateLogbookCommand(BaseCommand):
    desc = 'Creates a logbook from/to given dates'
    usage = 'CreateLogbook'
    parameters = [
        CommandParameter("date", Middleware.DATE, optional=True)
    ]

    def main(self) -> None:
        date = self.get_parameter_value("date", )

    def _get_parameters(self) -> List[CommandParameter]:
        return self.parameters


command = CreateLogbookCommand(__name__ == "__main__")
