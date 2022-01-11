interpolations = ['$NUM', '$SPACE']
comments = ['#', ';']


def interpret(processor, interpreter, command: str) -> bool:
    if not command.strip():
        return False
    token = processor.tokenize_command(command)
    interpreter.run_command(token)
    return True


def filter_num(text: str, value: str) -> str:
    """Filter the "$NUM" interpolation from a string

    Args:
        text (str): The text to filter
        value (str): The value to replace
    """
    return text.replace('$NUM', value)


def filter_space(text: str, value: str) -> str:
    """Filter the "$SPACE" interpolation from a string

    Args:
        text (str): The text to filter
        value (str): The value to replace
    """
    return text.replace('$SPACE', value)


def throw(code: object) -> None:
    """Throw an error

    Args:
        code (object): The error code
    """
    print(f'ERR {code}')
