# Actions module for lyon
from .util import filter_space, filter_num, interpret, throw
from .core import Command, CommandProcessor, CommandInterpreter, CommandTable
from .memory import Space, Num, Var
from .errs import FILE_ERR
from sys import exit

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
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    print(val, end='')


def outln(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    print(val)


def rdin(val: str) -> str:
    SPACE.set(input())


def clio(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    SPACE.clear()


def iowrt(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    SPACE.set(val)


def var(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    VAR.new(val)


def val(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    VAR.set(val)


def ldvar(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    SPACE.set(VAR.get(val))


def sum(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    NUM.add(val)


def sub(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    NUM.sub(val)


def mul(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    NUM.mul(val)


def div(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    NUM.div(val)


def run(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    try:
        with open(f'{val}') as f:
            TABLE.insert_commands(COMMANDS)
            for line in f:
                interpret(PROCESSOR, INTERPRETER, line)
    except Exception:
        throw(FILE_ERR)


def ext(val: str) -> None:
    exit()


# All <Command> objects
COMMANDS = [
    Command(name='out', action=out),
    Command(name='outln', action=outln),
    Command(name='rdin', action=rdin),
    Command(name='clio', action=clio),
    Command(name='iowrt', action=iowrt),
    Command(name='var', action=var),
    Command(name='val', action=val),
    Command(name='ldvar', action=ldvar),
    Command(name='sum', action=sum),
    Command(name='sub', action=sub),
    Command(name='mul', action=mul),
    Command(name='div', action=div),
    Command(name='run', action=run),
    Command(name='ext', action=ext)
]