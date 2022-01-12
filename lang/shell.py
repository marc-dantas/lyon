from rich.console import Console

CONSOLE = Console()


def print_header(title, subtitle=None) -> None:
    CONSOLE.print(f" [blue italic]{title}[/] ".center(80, '-'))
    if subtitle:
        CONSOLE.print(f" [blue bold]{subtitle}[/] ".center(80, '-'))


def print_info(message):
    CONSOLE.print(f' [blue bold]{message}[/] ')


def print_success(message):
    CONSOLE.print(f' [green bold]{message}[/] ')


def print_hint(hint: str) -> None:
    CONSOLE.print(f"\t-> [italic]{hint}[/]")


def get() -> str:
    CONSOLE.print('[yellow]>>>[/] ', end='')
    return input()
