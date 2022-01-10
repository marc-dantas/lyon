# Actions module for lyon
from util import filter_io, filter_num
from core import Command

# Main command actions (functions)


def out(val: str) -> None:
    val = filter_num(val, str(...))
    val = filter_io(val, str(...))
    print(val, end='')


def outln(val: str) -> None:
    val = filter_num(val, str(...))
    val = filter_io(val, str(...))
    print(val)


def rdin(val: str) -> str:
    return input()


def clio(val: str) -> None:
    print(val)


def iowrt(val: str) -> None:
    pass
    # TODO: Implement iowrt


def ldio(val: str) -> None:
    pass
    # TODO: Implement ldio


def var(val: str) -> None:
    pass
    # TODO: Implement var


def val(val: str) -> None:
    pass
    # TODO: Implement val


def load(val: str) -> None:
    pass
    # TODO: Implement load


def add(val: str) -> None:
    pass
    # TODO: Implement add


def sub(val: str) -> None:
    pass
    # TODO: Implement sub


def mul(val: str) -> None:
    pass 
    # TODO: Implement mul


def div(val: str) -> None:
    pass
    # TODO: Implement div


def runfile(val: str) -> None:
    pass
    # TODO: Implement runfile


def ext(val: str) -> None:
    pass
    # TODO: Implement ext


# All <Command> objects
COMMANDS = {
    'out': Command(name='out', action=out),
    'outln': Command(name='outln', action=outln),
    'rdin': Command(name='rdin', action=rdin),
    'clio': Command(name='clio', action=clio),
    'iowrt': Command(name='iowrt', action=iowrt),
    'ldio': Command(name='ldio', action=ldio),
    'var': Command(name='var', action=var),
    'val': Command(name='val', action=val),
    'load': Command(name='load', action=load),
    'add': Command(name='add', action=add),
    'sub': Command(name='sub', action=sub),
    'mul': Command(name='mul', action=mul),
    'div': Command(name='div', action=div),
    'runfile': Command(name='runfile', action=runfile),
    'ext': Command(name='ext', action=ext)
}
