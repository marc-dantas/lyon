from typing import Callable
from .util import throw
from .errs import INVALID_ARG, INVALID_COMMAND
from .data_models import *
from re import match


class CommandToken:

    def __init__(self, command: str,
                 parameter: String | Number = None) -> None:
        self._cmd = command
        self._param = parameter or 'None'

    @property
    def val(self) -> list[str | (String | Number)]:
        return [self._cmd, self._param]

    def __repr__(self) -> list:
        return [self._cmd, self._param]


class Command:

    def __init__(self, name: str, action: Callable) -> None:
        self._name = name
        self._action = action

    @property
    def name(self) -> str:
        return self._name

    @property
    def action(self) -> Callable:
        return self._action

    def __call__(self, argument) -> None:
        self.action(argument)


class CommandTable:
    
    def __init__(self) -> None:
        self._commands: list[Command] = []
    
    @property
    def commands(self) -> list[Command]:
        return self._commands

    def insert(self, command: Command) -> None:
        self._commands.append(command)

    def insert_commands(self, commands: list[Command]) -> None:
        for command in commands:
            self.insert(command)

    def exists(self, name: str) -> bool:
        return any(not not i for i in self.commands
                   if i.name == name)

    def get(self, name: str) -> Command:
        return next(i for i in self.commands
                    if i.name == name)

    def __repr__(self) -> str:
        return self._commands


class CommandProcessor:

    @staticmethod
    def format_cmd(command: str) -> str:
        return command.strip()
        
    def tokenize_command(self, command: str) -> CommandToken:
        format = self.format_cmd(command).split(' ', 1)
        if len(format) > 1:
            cmd, param = format
        else:
            cmd = format[0]
            param = '"None"'
        cmd = cmd.lower()
        token = None
        if Number.is_number(param):
            token = CommandToken(cmd, Number(param))
        elif String.is_string(param):
            token = CommandToken(cmd, String(param))
        else:
            throw(INVALID_ARG, '(command tokenization)')
            return CommandToken(cmd, String('" "'))
        return token


class CommandInterpreter:

    def __init__(self, command_table: CommandTable) -> None:
        self._command_table = command_table

    @property
    def command_table(self) -> CommandTable:
        return self._command_table

    def get_command(self, token: CommandToken) -> tuple:
        cmd, param = token.val
        if self.command_table.exists(cmd):
            cmd = self.command_table.get(cmd)
            return (cmd.action, param.get_value())
        return (None, None)

    def run_command(self, token: CommandToken) -> None:
        action, parameter = self.get_command(token)
        if action is not None or parameter is not None:
            action(parameter)
        else:
            throw(INVALID_COMMAND)
