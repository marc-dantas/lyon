# Actions module for lyon
from .util import filter_interpolations, interpret, throw
from .memory import Space, Num, Var
from .errs import FILE_ERR
from sys import exit
from .core import (Command,
                   CommandProcessor,
                   CommandInterpreter,
                   CommandTable)
from .expr import ConditionalExpression

# Memory
SPACE = Space()
NUM = Num()
VAR = Var()

# Command table, processing and interpreter
PROCESSOR = CommandProcessor()
TABLE = CommandTable()
INTERPRETER = CommandInterpreter(TABLE)


# Main command actions (functions)
def cmd_out(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    print(val, end='')


def cmd_outln(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    print(val)


def cmd_readin(val: str) -> str:
    SPACE.set(input())


def cmd_mclear(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    SPACE.clear()


def cmd_mwrite(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    SPACE.set(val)


def cmd_var(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    VAR.new(val)


def cmd_val(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    VAR.set(val)


def cmd_ldvar(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    SPACE.set(VAR.get(val))


def cmd_clearnum(val: str) -> None:
    NUM.clear()


def cmd_sum(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    NUM.add(val)


def cmd_sub(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    NUM.sub(val)


def cmd_mul(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    NUM.mul(val)


def cmd_div(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    NUM.div(val)


def cmd_run(val: str) -> None:
    try:
        with open(f'{val}', encoding='utf-8') as f:
            cmds = f.read().split('\n')
            for cmd in cmds:
                interpret(PROCESSOR, INTERPRETER, cmd)
    except Exception:
        throw(FILE_ERR, 'run')


def cmd_when(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    if ConditionalExpression(SPACE.value).evaluate():
        cmd_run(val)


def cmd_else(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    if not ConditionalExpression(SPACE.value).evaluate():
        cmd_run(val)


def cmd_while(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    expr = ConditionalExpression(SPACE.value).evaluate()
    while expr:
        cmd_run(val)


def cmd_fread(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}', 'r', encoding='utf-8') as f:
            SPACE.set(f.read())
    except Exception:
        throw(FILE_ERR, 'fread')


def cmd_fwrite(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}', 'w', encoding='utf-8') as f:
            f.write(SPACE.value)
    except Exception:
        throw(FILE_ERR, 'fwrite')


def cmd_fwriteln(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}', 'w', encoding='utf-8') as f:
            f.write(SPACE.value + '\n')
    except Exception:
        throw(FILE_ERR, 'fwriteln')


def cmd_ext(val: str) -> None:
    exit()


# All Commands
COMMANDS = [
    # Input/Output Commands
    Command(name='out', action=cmd_out),
    Command(name='outln', action=cmd_outln),
    Command(name='readin', action=cmd_readin),
    # IO Commands
    Command(name='mclear', action=cmd_mclear),
    Command(name='mwrite', action=cmd_mwrite),
    # Variable Commands
    Command(name='var', action=cmd_var),
    Command(name='val', action=cmd_val),
    Command(name='loadvar', action=cmd_ldvar),
    # Math Commands
    Command(name='clearnum', action=cmd_clearnum),
    Command(name='sum', action=cmd_sum),
    Command(name='sub', action=cmd_sub),
    Command(name='mul', action=cmd_mul),
    Command(name='div', action=cmd_div),
    # Flow Control Commands
    Command(name='runwhen', action=cmd_when),
    Command(name='runelse', action=cmd_else),
    Command(name='runwhile', action=cmd_while),
    # File commands
    Command(name='fread', action=cmd_fread),
    Command(name='fwrite', action=cmd_fwrite),
    Command(name='fwriteln', action=cmd_fwriteln),
    # Other commands
    Command(name='run', action=cmd_run),
    Command(name='ext', action=cmd_ext)
]
TABLE.insert_commands(COMMANDS)