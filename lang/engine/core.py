from typing import Callable
from .util import throw, comments


class CommandToken:

    def __init__(self, command: str, parameter: str = None) -> None:
        self._cmd = command
        self._param = parameter

    @property
    def val(self) -> str:
        return f'{self._cmd}:{self._param}'

    def __str__(self) -> str:
        return f'{self._cmd}:{self._param}'


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
        return self.get(name) is not None

    def get(self, name: str) -> Command:
        for command in self.commands:
            if command.name == name:
                return command
        return None

    def __repr__(self) -> str:
        return self._commands


class CommandProcessor:

    @staticmethod
    def format_cmd(command: str) -> tuple:
        format = tuple(i.strip() for i in command.split(' ', 1))
        return tuple(i for i in format if i)
        
    def tokenize_command(self, command: str) -> CommandToken:
        return CommandToken(*CommandProcessor.format_cmd(command))


class CommandInterpreter:

    def __init__(self, command_table: CommandTable) -> None:
        self._command_table = command_table

    @property
    def command_table(self) -> str:
        return self._command_table

    def run_command(self, token: CommandToken) -> object:
        cmd = (token.val).split(':')
        if self._command_table.exists(cmd[0]):
            return self._command_table.get(cmd[0]).action(cmd[1])
        elif cmd[0][0] in comments:
            return None
        else:
            throw(1)
            return None
