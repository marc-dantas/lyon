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
        base = base.replace(memspace.repr, str(memspace.value))
    return base


def throw(code: object) -> None:
    """Throw an error

    Args:
        code (object): The error code
    """
    Console().print(f'[red]ERROR: [italic bold]{code}[/][/]')
