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
def out(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    print(val, end='')


def outln(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    print(val)


def readin(val: str) -> str:
    SPACE.set(input())


def mclear(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    SPACE.clear()


def mwrite(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    SPACE.set(val)


def var(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    VAR.new(val)


def val(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    VAR.set(val)


def ldvar(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    SPACE.set(VAR.get(val))


def clearnum(val: str) -> None:
    NUM.clear()


def sum(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    NUM.add(val)


def sub(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    NUM.sub(val)


def mul(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    NUM.mul(val)


def div(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    NUM.div(val)


def run(val: str) -> None:
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
        run(val)


def cmd_else(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    if not ConditionalExpression(SPACE.value).evaluate():
        run(val)


def cmd_while(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    expr = ConditionalExpression(SPACE.value).evaluate()
    while expr:
        run(val)


def fread(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}', 'r', encoding='utf-8') as f:
            SPACE.set(f.read())
    except Exception:
        throw(FILE_ERR, 'fread')


def fwrite(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}', 'w', encoding='utf-8') as f:
            f.write(SPACE.value)
    except Exception:
        throw(FILE_ERR, 'fwrite')


def fwriteln(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}', 'w', encoding='utf-8') as f:
            f.write(SPACE.value + '\n')
    except Exception:
        throw(FILE_ERR, 'fwriteln')


def ext(val: str) -> None:
    exit()


# All <Command> objects
COMMANDS = [
    # Input/Output Commands
    Command(name='out', action=out),
    Command(name='outln', action=outln),
    Command(name='readin', action=readin),
    # IO Commands
    Command(name='mclear', action=mclear),
    Command(name='mwrite', action=mwrite),
    # Variable Commands
    Command(name='var', action=var),
    Command(name='val', action=val),
    Command(name='loadvar', action=ldvar),
    # Math Commands
    Command(name='clearnum', action=clearnum),
    Command(name='sum', action=sum),
    Command(name='sub', action=sub),
    Command(name='mul', action=mul),
    Command(name='div', action=div),
    # Flow Control Commands
    Command(name='runwhen', action=cmd_when),
    Command(name='runelse', action=cmd_else),
    Command(name='runwhile', action=cmd_while),
    # File commands
    Command(name='fread', action=fread),
    Command(name='fwrite', action=fwrite),
    Command(name='fwriteln', action=fwriteln),
    # Other commands
    Command(name='run', action=run),
    Command(name='ext', action=ext)
]
TABLE.insert_commands(COMMANDS)