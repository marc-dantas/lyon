from cmath import exp
from rich.console import Console

CONSOLE = Console()


def print_header(title, subtitle=None) -> None:
    CONSOLE.print(f"[blue italic]{title}[/]", style='green')
    if subtitle:
        CONSOLE.print(f"[blue bold]{subtitle}[/]", style='green')


def print_info(message):
    CONSOLE.print(f'[yellow bold]{message}[/] ')


def print_success(message):
    CONSOLE.print(message, style='green')


def print_hint(hint: str) -> None:
    CONSOLE.print(f"  [blue]→[/] [italic]{hint}[/]")


def get() -> str:
    CONSOLE.print('[yellow]>>>[/] ', end='')
    try:
        return input()
    except (Exception, KeyboardInterrupt):
        exit(1)