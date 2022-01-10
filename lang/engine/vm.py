from engine.core import Command
from engine.actions import COMMANDS
from engine.util import filter_io, filter_num

class ByteCode:
    def __init__(self, cmd_name: str, arg: str) -> None:
        self.arg = arg
        self.cmd = cmd_name
        pass

class VirtualMachine:
    def __init__(self):
        self.vars = {} # variable 
        self.space = "" # current loaded variable
        self.last_var = "" # kinda obvious
        self.commands = {
            'out': Command(name='out', action=self._out),
            'outln': Command(name='outln', action=self._outln),
            'rdin': Command(name='rdin', action=self._rdin),
            'clio': Command(name='clio', action=self._clio),
            'iowrt': Command(name='iowrt', action=self._iowrt),
            'ldio': Command(name='ldio', action=self._ldio),
            'var': Command(name='var', action=self._var),
            'val': Command(name='val', action=self._val),
            'load': Command(name='load', action=self._load),
            'add': Command(name='add', action=self._add),
            'sub': Command(name='sub', action=self._sub),
            'mul': Command(name='mul', action=self._mul),
            'div': Command(name='div', action=self._div),
            'runfile': Command(name='runfile', action=self._runfile),
            'ext': Command(name='ext', action=self._ext)
        }

    def call(self, name: str):
        cmd = self.commands.get(name)
        if cmd == None:
            self.vm_panic(1)
        else:
            cmd.action(self.space)
    def call_arg(self, name: str, arg: str):
        cmd = self.commands.get(name)
        if cmd == None:
            self.vm_panic(1)
        else:
            cmd.action(arg)
    def run_bytecode(self, code: ByteCode):
        if not code.arg:
                self.call(code.cmd)
        else:
            self.call_arg(code.cmd, code.arg)
    
    def run_bytecode_arr(self, bytecode):
        for code in bytecode:
            self.run_bytecode(code)

    def vm_panic(self, code: int):
        print(f"Virtual Machine PANIC! error code: {code}")
        exit(code+1)
    def _out(self, val: str) -> None:
        val = filter_num(val, str(...))
        val = filter_io(val, str(...))
        print(val, end='')

    def _outln(self, val: str) -> None:
        val = filter_num(val, str(...))
        val = filter_io(val, str(...))
        print(val)


    def _rdin(self, val: str) -> str:
        return input()


    def _clio(self, val: str) -> None:
        print(val)


    def _iowrt(self, val: str) -> None:
        pass
        # TODO: Implement iowrt


    def _ldio(self, val: str) -> None:
        pass
        # TODO: Implement ldio


    def _var(self, val: str) -> None:
        if not val:
            self.vm_panic(0)
        self.vars[val] = ""
        self.last_var = val
        # TODO: Implement var

    def _val(self, val: str) -> None:
        if not self.last_var:
            self.vm_panic(0)
        self.vars[self.last_var] = val
        # TODO: Implement val


    def _load(self, val: str) -> None:
        if self.vars.get(val) == None:
            self.space = val
        self.space = self.vars[val]
        # TODO: Implement load


    def _add(self, val: str) -> None:
        pass
        # TODO: Implement add


    def _sub(self, val: str) -> None:
        pass
        # TODO: Implement sub


    def _mul(self, val: str) -> None:
        pass 
        # TODO: Implement mul


    def _div(self, val: str) -> None:
        pass
        # TODO: Implement div


    def _runfile(self, val: str) -> None:
        pass
        # TODO: Implement runfile


    def _ext(self, val: str) -> None:
        pass
        # TODO: Implement ext
