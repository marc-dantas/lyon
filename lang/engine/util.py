from rich.console import Console


interpolations = ['@NUM', '@SPACE']


def interpret(processor, interpreter, command: str) -> bool:
    if not command.strip():
        return False
    token = processor.tokenize_command(command)
    interpreter.run_command(token)
    return True


def filter_interpolations(base: str, *args) -> str:
    """Filter the interpolations from a string

    Args:
        base (str): The text to filter
        *args: The interpolations (Memory objects) to filter
    """
    for memspace in args:
        base = str(base).replace(memspace.repr, str(memspace.value))
    return base


def throw(value: object, at: str = '') -> None:
    """Throw an error

    Args:
        value (object): The error code or error message
    """
    if not at:
        Console().print(f'[red]ERROR: [italic bold]{value}[/][/]')
    else:
        Console().print(f'[red]ERROR → [yellow bold]{at}[/]: [italic bold]{value}[/][/]')