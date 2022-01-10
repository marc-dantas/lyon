# import engine
import shell
from engine.vm import VirtualMachine, ByteCode

# TODO: Implementation of command interpretation
if __name__ == '__main__':
    shell.print_header(title='Lyon', subtitle='The command language')
    vm = VirtualMachine()
    while True:
        cmd = shell.get()
        splited_cmd = cmd.split(" ")
        cmdname = splited_cmd[0]
        arg = ""
        if len(splited_cmd) > 1:
            arg = splited_cmd[1]
        code = ByteCode(cmdname, arg)
        vm.run_bytecode(code=code)
