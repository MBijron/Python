import sys
from typing import Any

from commands.base.command_parameter import CommandParameter

class CommandBase:
    desc = 'No description available for this command'
    usage = 'No Usage available for this command'
    settings: [str] = []
    parameters: [CommandParameter] = [

    ]

    def main(self) -> None:
        raise NotImplementedError

    def get_parameter_value(self, name: str) -> Any:
        for parameter in self.parameters:
            if parameter.get_name() == name:
                return parameter.get_value()
        raise Exception("No parameter with the name " + name + " was defined")

    def __check_parameter_business_rules(self) -> None:
        optional_encountered = False
        for parameter in self.parameters:
            if parameter.is_optional():
                optional_encountered = True
            elif optional_encountered:
                raise Exception("not-optional parameters can't be defined after optional parameters")

    def __appoint_parameter_values(self, arguments) -> None:
        name = None
        for parameter in arguments[1:]:
            if parameter.startswith("--"):
                self.__validate_setting(parameter)
                self.settings.append(parameter[2:])
            if parameter.startswith("-"):
                self.__validate_parameter_name(parameter)
                name = parameter[1:]
            else:
                if name is not None:
                    self.__assign_named_parameter(name, parameter)
                    name = None
                else:
                    self.__assign_next_parameter(parameter)

    def __assign_named_parameter(self, name, value) -> None:
        for parameter in self.parameters:
            if parameter.get_name() == name:
                parameter.set_value(value)
                return
        raise Exception("No parameter with name " + name + " exists")

    def __assign_next_parameter(self, value) -> None:
        for parameter in self.parameters:
            if not parameter.has_value():
                parameter.set_value(value)
                return
        raise Exception("Parameter " + value + " cannot be assigned. Command doesnt take any more commands")

    def __validate_setting(self, value) -> None:
        if len(value) < 2:
            raise Exception("-- should be followed by a setting name without whitespaces")

    def __validate_parameter_name(self, value) -> None:
        if len(value) < 1:
            raise Exception("- should be followed by a parameter name")

    def __check_parameter_values(self) -> None:
        for parameter in self.parameters:
            if not parameter.check():
                raise Exception("Parameter " + parameter.get_value() + " has the wrong value")

    def __run(self, args) -> None:
        self.__check_parameter_business_rules()
        self.__appoint_parameter_values(args)
        self.__check_parameter_values()
        self.__args = args
        self.main()

    def __init__(self, run) -> None:
        if run:
            self.__run(sys.argv)
