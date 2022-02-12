from .util import throw
from .errs import INVALID_ARG, INVALID_COMMAND, INVALID_SYNTAX
from .data_models import *
from re import match


class CommandToken:

    def __init__(self, command: str,
                 parameter: String | Number = None) -> None:
        self._cmd = command
        self._param = parameter or 'None'

    @property
    def val(self) -> list[str, String | Number]:
        return [self._cmd, self._param]

    def __repr__(self) -> list:
        return [self._cmd, self._param]


class Command:
    
    SYNTAX = r'([a-zA-Z]+) ("(.+)"|[+-]?\d+(?:\.\d+)?)'

    def __init__(self, name: str, action: 'function') -> None:
        self._name = name
        self._action = action

    @property
    def name(self) -> str:
        return self._name

    @property
    def action(self) -> 'function':
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
    
    def string_token(self,
                     command: str,
                     parameter: str) -> CommandToken:
        return CommandToken(command, String(parameter))
    
    def number_token(self,
                     command: str,
                     parameter: str) -> CommandToken:
        return CommandToken(command, Number(parameter))
        
    def tokenize_command(self, command: str) -> CommandToken:
        token = None
        cmd_format = self.format_cmd(command).split(' ', 1)
        cmd, param = (cmd_format if len(cmd_format) > 1
                      else (cmd_format[0], '"None"'))
        cmd = cmd.lower()
        #if not match(Command.SYNTAX, command):
        #    throw(INVALID_SYNTAX, cmd)
        #    return CommandToken(cmd, String('" "'))
        if Number.is_number(param):
            token = self.number_token(cmd, param)
        elif String.is_string(param):
            token = self.string_token(cmd, param)
        else:
            throw(INVALID_ARG, command)
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
        return (cmd, None)

    def run_command(self, token: CommandToken) -> None:
        cmd, parameter = self.get_command(token)
        if parameter is not None:
            cmd(parameter)
        else:
            throw(INVALID_COMMAND, f"\"{cmd}\"")
