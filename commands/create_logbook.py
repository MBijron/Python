from commands.base.command_parameter import CommandParameter
from commands.base.middleware import Middleware
from commands.base.command_base import CommandBase


class CreateLogbookCommand(CommandBase):
    desc = 'Creates a logbook from/to given dates'
    usage = 'CreateLogbook'
    parameters = [
        CommandParameter("date", Middleware.DATE, optional=True)
    ]

    def main(self) -> None:
        date = self.get_parameter_value("date", )


command = CreateLogbookCommand(__name__ == "__main__")
