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
- Flow Control
    + `runif <file>`
    + `runelse <file>`
    + `runwhile <file>`
- File Commands
    + `fread <file>`
    + `fwrite <file>`
    + `fwriteln <file>`
- Other commands
    + `run <file>` - Runs a file
    + `ext` - Exit lyon

<br>

- [Input/Output](./input-output.md)
- [IO Commands](./io-commands.md)
- [Variable commands](./variable-commands.md)
- [Math commands](./math-commands.md)
- [Flow Control](./flow-control.md)
- [File Commands](./file-commands.md)

<hr>

### Error Codes
- 0: Unknown error (Default Error)
- 1: Invalid command (Unknown Command Error)
- 2: File Error
- 3: Invalid argument (Name Error)
- 4: Variable Error or Variable not found

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
lyon has a different way of interpreting files and folders, like folders being programs and files being functions. So you can use a manager to create programs (folders) that contain various functions (files).

<hr>

### Using Lyon
- To start the lyon interactive shell, type `lyon -s` or `lyon --shell`
#### Lyon Management
Lyon has a program that manages lyon programs (like a NPM).
##### Usage
- To use the management mode, use `lyon -m <command>` or `lyon --manage <command>`
    + Commands
        + `new <name>` - Creates a new lyon program
        + `run <program_path>` - Runs a lyon program
        + `rundebug <program_path>` - Runs a lyon program with debug messages.
    + Program Structure (Tree)
      + [program name] (folder [program])
        + src (folder)
          + main.lyon (file [function])
          + ... (files)
      + lyon.json (file)
- To run a single command, type `lyon -c <value>` or `lyon --command <value>`.

### Condition Expressions
- Condition Expressions are used to check a test
- To use this, use the `iowrt` command to write a expression
    + `iowrt @SPACE==None`
    + & Checking with `runif`, `runelse` or `runwhile`
        + `runif test.lyon`
        + `runelse falsetest.lyon`
        + `runwhile whiletest.lyon`
- #### Attention: The expressions (for now) will consider spaces around the operator, such as `abc == abc` will return false, as the first value is "abc " and the second is " abc". But if you use `abc==abc` (no spaces around the operator) it will return true