# Lyon Documentation
By [@marc-dantas](https://gitub.com/marc-dantas)

<hr>

### All commands
- Input/Output
    + `out <value>`
    + `outln <value>`
    + `rdin`
- IO Commands
    + `clio`
    + `iowrt <value>`
    + `ldio`
- Variable commands
    + `var <name>`
    + `val <value>`
    + `load <name>`
- Math commands
    + `add <number>`
    + `sub <number>`
    + `mul <number>`
    + `div <number>`
- Other commands
    + `runfile <file>` - Runs a file
    + `exit` - Exit lyon

<br>

- [Input/Output](./input-output.md)
- [IO Commands](./io-commands.md)
- [Variable commands](./variable-commands.md)
- [Math commands](./math-commands.md)

<hr>

### Error Codes
- 0: Unknown error
- 1: Invalid command
- 2: Invalid syntax

<hr>

### Memory
- `IO`: The space in the memory where the input and general values is stored.
    + Representation: `$IO`
<br><br>
- `NUM`: The space in the memory where the numbers are stored.
    + Representation: `$NUM`