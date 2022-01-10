# import engine
import shell
from engine.core import *
from engine.actions import *


if __name__ == '__main__':
    shell.print_header(title='Lyon', subtitle='The command language')
    while True:
        cmd = shell.get()
        # FIXME: Temporary test
        table = CommandTable()
        insert_commands(table)
        interpreter = CommandInterpreter(cmd, table)
        interpreter.run_command()