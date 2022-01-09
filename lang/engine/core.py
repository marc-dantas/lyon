from typing import Callable
from util import throw


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

    def __str__(self) -> str:
        return self._name

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

    def exists(self, command: str) -> bool:
        return any(cmd.name == command for cmd in self._commands)

    def get(self, name: str) -> Command | bool:
        for command in self._commands:
            if command.name == name:
                return command
        return None

    def __repr__(self) -> str:
        return self._commands


class CommandInterpreter:

    def __init__(self, command: str, command_table: CommandTable) -> None:
        self._command = command
        self._command_table = command_table
    
    def format_cmd(self) -> tuple:
        format = tuple(i.strip() for i in self._command.split(' ', 1))
        return tuple(i for i in format if i)

    def is_parameterized(self) -> bool:
        return len(self.format_cmd()) > 1

    @property
    def command(self) -> str:
        return self._command

    def run_command(self) -> object:
        cmd = (CommandToken(*self.format_cmd()).val).split(':')
        if self._command_table.exists(cmd[0]):
            return self._command_table.get(cmd[0]).action(cmd[1])
        throw(1)
        return None
