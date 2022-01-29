# Actions module for lyon
from .util import filter_interpolations, interpret, throw
from .memory import Space, Num, Var
from .errs import FILE_ERR
from sys import exit
from .core import (
    Command,
    CommandProcessor,
    CommandInterpreter,
    CommandTable,
    ExpressionParser
)

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
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}') as f:
            cmds = f.read().split('\n')
            for cmd in cmds:
                interpret(PROCESSOR, INTERPRETER, cmd)
    except Exception:
        throw(FILE_ERR)


def runif(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    expr = ExpressionParser().evaluate(SPACE.value)
    if expr:
        run(val)


def runelse(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    expr = ExpressionParser().evaluate(SPACE.value)
    if not expr:
        run(val)


def runwhile(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    expr = ExpressionParser().evaluate(SPACE.value)
    while expr:
        run(val)
        expr = ExpressionParser().evaluate(SPACE.value)


def fread(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}', 'r') as f:
            SPACE.set(f.read())
    except Exception:
        throw(FILE_ERR)
 

def fwrite(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}', 'w') as f:
            f.write(SPACE.value)
    except Exception:
        throw(FILE_ERR)


def fwriteln(val: str) -> None:
    val = filter_interpolations(val, SPACE, NUM)
    try:
        with open(f'{val}', 'w') as f:
            f.write(SPACE.value + '\n')
    except Exception:
        throw(FILE_ERR)


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
    Command(name='sum', action=sum),
    Command(name='sub', action=sub),
    Command(name='mul', action=mul),
    Command(name='div', action=div),
    # Flow Control Commands
    Command(name='runif', action=runif),
    Command(name='runelse', action=runelse),
    Command(name='runwhile', action=runwhile),
    # File commands
    Command(name='fread', action=fread),
    Command(name='fwrite', action=fwrite),
    Command(name='fwriteln', action=fwriteln),
    # Other commands
    Command(name='run', action=run),
    Command(name='ext', action=ext)
]
TABLE.insert_commands(COMMANDS)