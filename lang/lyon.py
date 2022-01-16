from engine.actions import COMMANDS
import shell
import engine.core
import engine.util

# Constants
TABLE = engine.core.CommandTable()
TABLE.insert_commands(COMMANDS)
PROCESSOR = engine.core.CommandProcessor()
INTERPRETER = engine.core.CommandInterpreter(TABLE)


def main() -> None:
    shell.print_header('Lyon', 'Interactive console')
    shell.print_hint('Type "ext" to [bold]exit[/]')
    shell.print_hint('Type "run <filename>" to [bold]run[/] a file (function)')
    shell.print_hint('See docs at <https://github.com/marc-dantas/lyon/blob/master/docs/index.md>')
    while True:
        cmd = shell.get()
        res = engine.util.interpret(PROCESSOR, INTERPRETER, cmd)
        if not res:
            continue


if __name__ == '__main__':
    main()
