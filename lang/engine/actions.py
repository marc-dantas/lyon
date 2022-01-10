# Actions module for lyon
from .util import filter_space, filter_num
from .core import Command
from .memory import Space, Num, Var

# Memory
SPACE = Space()
NUM = Num()
VAR = Var()


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


def load(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    SPACE.set(VAR.get(val))


def add(val: str) -> None:
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


def runfile(val: str) -> None:
    val = filter_num(val, str(NUM.value))
    val = filter_space(val, str(SPACE.value))
    # TODO: Implement runfile


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
    Command(name='load', action=load),
    Command(name='add', action=add),
    Command(name='sub', action=sub),
    Command(name='mul', action=mul),
    Command(name='div', action=div),
    Command(name='runfile', action=runfile),
    Command(name='ext', action=ext)
]


def insert_commands(table) -> None:
    for command in COMMANDS.values():
        table.insert(command)
