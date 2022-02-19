from .util import filter_interpolations
from .models import *
from .memory import *
from .errs import INVALID_COMMAND

# Memory
SPACE = Space()
NUM = Num()
VAR = Var()
PARAM = Param()
CMP = Cmp()

# General constants
INTERPOLATIONS = (SPACE, NUM, PARAM)
TYPES = (String, Number)


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


class CommandLexer:

    @staticmethod
    def _format_cmd(command: str) -> tuple[str, str]:
        f = command.strip().split(' ', 1)
        return (f[0].lower(), f[-1]) if len(f) > 1 else (f[0], '"None"')
    
    def _create_token(self, cmd_name: str, param: str) -> CommandToken:
        for cls in TYPES:
            if cls.match_syntax(param):
                return CommandToken(cmd_name, cls(param))
        throw(INVALID_ARG, cmd_name, 'Invalid type literal.')
        return CommandToken(cmd_name, String('""'))
    
    def tokenize_command(self, command: str) -> CommandToken:
        cmd_name, param = self._format_cmd(command)
        param = filter_interpolations(param, *INTERPOLATIONS)
        return self._create_token(cmd_name, param)


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
