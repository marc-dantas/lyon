from typing import Callable


class Token:
    
    def __init__(self, type: object, value: object) -> None:
        super().__init__()
        self._type = type
        self._value = value

    @property
    def type(self) -> object:
        return self._type

    @property
    def value(self) -> object:
        return self._value

    def __str__(self) -> str:
        return f'{self.type}.{self.value}'


class Command:

    def __init__(self, name: str, action: Callable,
                have_param: bool = False) -> None:
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
        self.__command = command

    @property
    def command(self) -> str:
        return self.__command

    def tokenize(self) -> list:
        # TODO: Implement tokenization
        pass

    def parse(self) -> list:
        # TODO: Implement parsing
        pass

    def __call__(self, *args, **kwargs) -> None:
        return self.parse(self.tokenize())
