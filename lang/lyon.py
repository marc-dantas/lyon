from engine.actions import COMMANDS
from sys import argv
from manager import *
import shell
import engine.core
import engine.util

# Constants
TABLE = engine.core.CommandTable()
TABLE.insert_commands(COMMANDS)
PROCESSOR = engine.core.CommandProcessor()
INTERPRETER = engine.core.CommandInterpreter(TABLE)
ARGS = {
    'manage': ('--manage', '-m'),
    'shell': ('--shell', '-s')
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
    shell.print_header('Lyon', 'Interactive SHELL')
    shell.print_hint('Type "ext" to [bold]exit[/]')
    shell.print_hint('Type "run <filename>" to [bold]run[/] a file (function)')
    shell.print_hint('See docs at <https://github.com/marc-dantas/lyon/blob/master/docs/index.md>')
    shell.print_info('Copyright (c) 2022 - @marc-dantas')
    shell.print_info('Licensed under the MIT License')
    while True:
        cmd = shell.get()
        res = engine.util.interpret(PROCESSOR, INTERPRETER, cmd)
        if not res:
            continue


def main():
    if len(argv) > 1:
        if argv[1] in ARGS['manage']:
            manage()
        elif argv[1] in ARGS['shell']:
            start_shell()
        else:
            show_info('Lyon: [red]Invalid command or argument syntax[/]')
    else:
        show_info('Lyon')
    exit(1)


if __name__ == '__main__':
    main()
