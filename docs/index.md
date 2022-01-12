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
- Variable commands
    + `var <name>`
    + `val <value>`
    + `ldvar <name>`
- Math commands
    + `sum <number>`
    + `sub <number>`
    + `mul <number>`
    + `div <number>`
- Other commands
    + `runfile <file>` - Runs a file
    + `ext` - Exit lyon

<br>

- [Input/Output](./input-output.md)
- [IO Commands](./io-commands.md)
- [Variable commands](./variable-commands.md)
- [Math commands](./math-commands.md)

<hr>

### Error Codes
- 0: Unknown error (Default Error)
- 1: Invalid command (Unknown Command Error)
- 2: File Error
- 3: Invalid argument (Name Error)
- 4: Variable Error or Variable not found

<hr>

### Comments
- Lyon defaults to two types of comment representation: `#` and `;`
- Syntax for the hashtag: `# <some text>`
- Syntax for the semicolon: `; <some text>`

<hr>

### Memory
- `@SPACE`: The space in the memory where the input and general values is stored.
    + Representation: `@SPACE` -> example: `outln @SPACE` (prints the `@SPACE` value)
    + NOTE: The default value is "None"
<br><br>
- `@NUM`: The space in the memory where the numbers are stored.
    + Representation: `@NUM` -> example: `outln @NUM` (prints the `@NUM` value)
    + NOTE: The default value is 0.

<hr>

### How lyon interpret files, commands & folders...?
lyon has a different way of interpreting files and folders, like folders being programs and files being functions. So you can use a manager (Like LyonManager) to create programs (folders) that contain various functions (files).

<hr>

### LyonManager
LyonManager is a program that manages lyon programs (like a NPM).
- Usage
    + `$ [lyonmanager] <command> <args>`
    + Commands
        + `new <name> <version>` - Creates a new lyon program
        + `run <program_path>` - Runs a lyon program