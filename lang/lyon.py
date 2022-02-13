from manager import *
from engine.actions import PROCESSOR, INTERPRETER
from sys import argv
from engine import util, VERSION
import shell

# Constants
ARGS = {
    'manage': ('--manage', '-m'),
    'shell': ('--shell', '-s'),
    'simpleshell': ('--simple-shell', '-ss'),
    'command': ('--command', '-c'),
    'version': ('--version', '-v'),
}


def manage():
    if argv[2] == 'new' and len(argv) >= 3:
        create_program(argv[3])
    elif argv[2] == 'rundebug' and len(argv) >= 3:
        run_program(argv[3])
    elif argv[2] == 'run' and len(argv) >= 3:
        run_program(argv[3], debug=False)
    else:
        show_info('Lyon: [red]Invalid command or argument syntax[/]')
    exit(1)


def start_shell() -> None:
    shell.print_header(f'Lyon {VERSION} <https://marc-dantas.github.io/lyon/>', 'Interactive SHELL')
    shell.print_hint('Type "ext" to [bold]exit[/]')
    shell.print_hint('Type "run <filename>" to [bold]run[/] a file (function)')
    shell.print_hint('Type "hlp" to [bold]show the help[/]')
    shell.print_hint('See docs at <https://github.com/marc-dantas/lyon/blob/master/docs/index.md>')
    shell.print_info('Copyright (c) 2022 - @marc-dantas.')
    shell.print_info('Licensed under the MIT License.')
    while True:
        cmd = shell.get()
        res = util.interpret(PROCESSOR, INTERPRETER, cmd)
        if not res:
            continue

def start_simple_shell():
    while True:
        cmd = shell.get()
        res = util.interpret(PROCESSOR, INTERPRETER, cmd)
        if not res:
            continue


def run_cmd(cmd: str) -> None:
    res = util.interpret(PROCESSOR, INTERPRETER, cmd)
    if not res:
        return


def main():
    if len(argv) > 1:
        if argv[1] in ARGS['manage'] and len(argv) > 3:
            manage()
        elif argv[1] in ARGS['shell'] and len(argv) == 2:
            start_shell()
        elif argv[1] in ARGS['simpleshell'] and len(argv) == 2:
            start_simple_shell()
        elif len(argv) == 1:
            start_shell()
        elif argv[1] in ARGS['command'] and len(argv) > 2:
            run_cmd(argv[2])
        elif argv[1] in ARGS['version'] and len(argv) == 2:
            print_success(VERSION)
        else:
            show_info('Lyon: [red]Invalid command or argument syntax[/]')
    else:
        start_shell()
    exit(1)


if __name__ == '__main__':
    main()
