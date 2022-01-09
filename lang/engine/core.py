from typing import Callable


class Error:

    def __init__(self, code: int = 0) -> None:
        self._code = code

    def throw(self) -> None:
        print(f'Error: {self._code}')


class ErrorCode:

    def __new__(cls, value: int) -> int:
        return super().__new__(cls, value)

    def __init__(self, value: int) -> None:
        self._value = value
    
    @property
    def code(self) -> int:
        return self._value

    def __repr__(self) -> int:
        return self._value


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

    def get(self, name: str) -> Command | bool:
        for command in self._commands:
            if command.name == name:
                return command
        return False

    def __repr__(self) -> str:
        return self._commands


class CommandInterpreter:

    def __init__(self, command: str, command_table: CommandTable) -> None:
        self._command = command
        self._command_table = command_table
    
    def format_cmd(self) -> tuple:
        return tuple(i for i in self.command.split(' ', 1) if i)

    def is_parameterized(self) -> bool:
        return len(self.format_cmd()) > 1

    @property
    def command(self) -> str:
        return self._command

    def interpret_command(self) -> Command | ErrorCode:
        cmd = (CommandToken(*self.format_cmd()).val).split(':')[0]
        if self.command_table.get(cmd):
            return self.command_table.get(cmd)
        return ErrorCode(1)
