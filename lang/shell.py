from cmath import exp
from rich.console import Console

CONSOLE = Console()


def print_header(title, subtitle=None) -> None:
    CONSOLE.print(f" [blue italic]{title}[/] ".center(50, '-'), style='green')
    if subtitle:
        CONSOLE.print(f" [blue bold]{subtitle}[/] ".center(48, '-'), style='green')


def print_info(message):
    CONSOLE.print(f'[blue bold]{message}[/] ')


def print_success(message):
    CONSOLE.print(f'[green bold]{message}[/] ')


def print_hint(hint: str) -> None:
    CONSOLE.print(f"  → [italic]{hint}[/]")


def get() -> str:
    CONSOLE.print('[yellow]>>>[/] ', end='')
    try:
        return input()
    except (Exception, KeyboardInterrupt):
        exit(1)