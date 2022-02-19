from msilib.schema import tables
from . import HELP
from .util import interpret, throw
from .errs import FILE_ERR
from sys import exit
from .core import *

# Command table, processing and interpreter
LEXER = CommandLexer()
TABLE = CommandTable()
INTERPRETER = CommandInterpreter(TABLE)

# Main command actions (functions)
def cmd_out(val: object) -> None:
    print(val, end='')


def cmd_outln(val: object) -> None:
    print(val)


def cmd_readin(val: object) -> None:
    SPACE.set(input())


def cmd_mclear(val: object) -> None:
    SPACE.clear()


def cmd_mwrite(val: object) -> None:
    SPACE.set(val)


def cmd_var(val: object) -> None:
    VAR.new(val)


def cmd_val(val: object) -> None:
    VAR.set(val)


def cmd_clearvar(val: object) -> None:
    VAR.clear()


def cmd_loadvar(val: object) -> None:
    SPACE.set(VAR.get(val))


def cmd_clearnum(val: object) -> None:
    NUM.clear()


def cmd_sum(val: object) -> None:
    NUM.add(val)


def cmd_sub(val: object) -> None:
    NUM.sub(val)


def cmd_mul(val: object) -> None:
    NUM.mul(val)


def cmd_div(val: object) -> None:
    NUM.div(val)


def cmd_setcmp(val: object) -> None:
    CMP.set(val)


def cmd_clearcmp(val: object) -> None:
    CMP.clear()


def cmd_call(val: object) -> None:
    try:
        with open(f'{val}', encoding='utf-8') as f:
            cmds = f.read().split('\n')
            for cmd in cmds:
                interpret(LEXER, INTERPRETER, cmd)
    except Exception as err:
        throw(FILE_ERR, 'call', err)


def cmd_pcall(val: object) -> None:
    try:
        PARAM.set(SPACE.value)
        with open(f'{val}', encoding='utf-8') as f:
            cmds = f.read().split('\n')
            for cmd in cmds:
                interpret(LEXER, INTERPRETER, cmd)
        PARAM.clear()
    except Exception as e:
        throw(FILE_ERR, 'pcall', e)


def cmd_callge(val: object) -> None:
    if CMP.compare('ge'):
        cmd_call(val)


def cmd_callle(val: object) -> None:
    if CMP.compare('le'):
        cmd_call(val)


def cmd_callgt(val: object) -> None:
    if CMP.compare('gt'):
        cmd_call(val)


def cmd_calllt(val: object) -> None:
    if CMP.compare('lt'):
        cmd_call(val)


def cmd_callne(val: object) -> None:
    if CMP.compare('ne'):
        cmd_call(val)


def cmd_calleq(val: object) -> None:
    if CMP.compare('eq'):
        cmd_call(val)


def cmd_fread(val: object) -> None:
    try:
        with open(f'{val}', 'r', encoding='utf-8') as f:
            SPACE.set(f.read())
    except Exception:
        throw(FILE_ERR, 'fread')


def cmd_fwrite(val: object) -> None:
    try:
        with open(f'{val}', 'w', encoding='utf-8') as f:
            f.write(SPACE.value)
    except Exception:
        throw(FILE_ERR, 'fwrite')


def cmd_hlp(val: object) -> None:
    print(HELP)


def cmd_typeof(val: object) -> None:
    t = None
    if Number.match_syntax(str(val)):
        t = 'Number'
    elif String.match_syntax(f'"{val}"'):
        t = 'String'
    cmd_outln(t)


def cmd_ext(val: object) -> None:
    exit()


# All Commands
COMMANDS = [
    # Input/Output Commands
    Command(name='out', action=cmd_out),
    Command(name='outln', action=cmd_outln),
    Command(name='readin', action=cmd_readin),
    # IO Commands
    Command(name='clear_mem', action=cmd_mclear),
    Command(name='mem_write', action=cmd_mwrite),
    # Variable Commands
    Command(name='var', action=cmd_var),
    Command(name='val', action=cmd_val),
    Command(name='clear_var', action=cmd_clearvar),
    Command(name='load_var', action=cmd_loadvar),
    # Math Commands
    Command(name='clear_num', action=cmd_clearnum),
    Command(name='sum', action=cmd_sum),
    Command(name='sub', action=cmd_sub),
    Command(name='mul', action=cmd_mul),
    Command(name='div', action=cmd_div),
    # Comparison & Flow Control commands
    Command(name='call_ge', action=cmd_callge),
    Command(name='call_le', action=cmd_callle),
    Command(name='call_gt', action=cmd_callgt),
    Command(name='call_lt', action=cmd_calllt),
    Command(name='call_ne', action=cmd_callne),
    Command(name='call_eq', action=cmd_calleq),
    Command(name='cmp', action=cmd_setcmp),
    Command(name='clear_cmp', action=cmd_clearcmp),
    # File commands
    Command(name='file_read', action=cmd_fread),
    Command(name='file_write', action=cmd_fwrite),
    # Other commands
    Command(name='hlp', action=cmd_hlp),
    Command(name='call', action=cmd_call),
    Command(name='param_call', action=cmd_pcall),
    Command(name='typeof', action=cmd_typeof),
    Command(name='ext', action=cmd_ext)
]
TABLE.insert_commands(COMMANDS)