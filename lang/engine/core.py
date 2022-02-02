from typing import Callable
from .util import throw
from .errs import INVALID_ARG, INVALID_COMMAND
from .memory import Num
from re import match

OPERATORS = {
    '==': r'.+\=.+',
    '>': r'.+\>.+',
    '<': r'.+\<.+'
}


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
        return any(not not i for i in self.commands
                   if i.name == name)

    def get(self, name: str) -> Command:
        return next(i for i in self.commands
                    if i.name == name)

    def __repr__(self) -> str:
        return self._commands


class CommandProcessor:

    @staticmethod
    def format_cmd(command: str) -> tuple:
        format = tuple(i.lstrip() for i in command.split(' ', 1))
        return tuple(i for i in format if i)
        
    def tokenize_command(self, command: str) -> CommandToken:
        return CommandToken(*CommandProcessor.format_cmd(command))


class CommandInterpreter:

    def __init__(self, command_table: CommandTable) -> None:
        self._command_table = command_table

    @property
    def command_table(self) -> list[Command]:
        return self._command_table

    def get_command(self, token: CommandToken) -> tuple:
        cmd = (token.val).split(':', 1)
        if self._command_table.exists(cmd[0]):
            return (self._command_table.get(cmd[0]).action, cmd[1])
        return (None, None)

    def run_command(self, token: CommandToken) -> None:
        action, parameter = self.get_command(token)
        if action is not None or parameter is not None:
            action(parameter)
        else:
            throw(INVALID_COMMAND)


class ExpressionParser:

    def evaluate(self, expr: str) -> bool:
        left, right, op = self.tokenize_expr(expr)
        if not all([left, right, op]):
            return False
        if Num.is_number(left) and Num.is_number(right):
            return eval(f'{float(left)}{op}{float(right)}')
        try:
            return eval(f'"{left}"{op}"{right}"')
        except Exception:
            return False

    def tokenize_expr(self, string: str) -> tuple[str, str, str]:
        if not string:
            return ('', '', '')
        for op, regex in OPERATORS.items():
            if match(regex, string):
                left, right = string.split(op, 1)
                return (left, right, op)
        return ('', '', '')
