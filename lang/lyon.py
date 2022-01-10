# import engine
import shell
import engine.core
import engine.actions

# Constants
TABLE = engine.core.CommandTable()
TABLE.insert_commands(engine.actions.COMMANDS)
PROCESSOR = engine.core.CommandProcessor()
INTERPRETER = engine.core.CommandInterpreter(TABLE)


def main() -> None:
    shell.print_header(title='Lyon', subtitle='The command language')
    shell.print_hint('Type "ext" to exit')
    while True:
        cmd = shell.get()
        token = PROCESSOR.tokenize_command(cmd)
        INTERPRETER.run_command(token)


if __name__ == '__main__':
    main()