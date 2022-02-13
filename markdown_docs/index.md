# Lyon Documentation
By [@marc-dantas](https://gitub.com/marc-dantas)

<hr>

### All commands
- Input/Output
    + `out <value>`
    + `outln <value>`
    + `readin`
- IO Commands
    + `mclear`
    + `mwrite <value>`
- Variable commands
    + `var <name>`
    + `val <value>`
    + `loadvar <name>`
- Math commands
    + `clearnum`
    + `sum <number>`
    + `sub <number>`
    + `mul <number>`
    + `div <number>`
- Flow Control
    + `runwhen <file>`
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

### Data types
- `String`: is a sequence of characters (text) and delimited by double quotes (`"`).
- `Number`: represent a integer or a real number. (decimal cases separated by a dot (`.`))

<hr>

### Memory
- `@SPACE`: The space in the memory where the input and general values is stored.
    + Representation: `@SPACE` → example: `outln "@SPACE"` (prints the `@SPACE` value)
    + NOTE: The default value is "None"
<br><br>
- `@NUM`: The space in the memory where the numbers are stored.
    + Representation: `@NUM` → example: `outln "@NUM"` (prints the `@NUM` value)
    + NOTE: The default value is 0.

<hr>

### How lyon interpret files, commands & folders...?
lyon has a different way of interpreting files and folders, like folders being programs and files being functions. So you can use a manager to create programs (folders) that contain various functions (files).

<hr>

### Using Lyon
- To start Lyon's interactive shell, type `lyon -s`, `lyon --shell` or don't enter any parameters.
#### Lyon Management
Lyon has a program that manages lyon programs
##### Usage
- To use the management mode, use `lyon -m <command>` or `lyon --manage <command>`
    + Commands
        + `new <name>` → Creates a new lyon program
        + `run <program_path>` → Runs a lyon program
        + `rundebug <program_path>` → Runs a lyon program with debug messages.
    + Program Structure (Tree)
      + [program name] (folder [program])
        + src (folder)
          + main.lyon (file [function])
          + ... (files)
      + lyon.json (file)
- To run a single command, type `lyon -c <value>` or `lyon --command <value>`.

<hr>

### Lyon Versions
Lyon versions start at 1.0. There are three "version tags": `DEV` to indicate that it is an unreleased version, `RELEASE` to indicate that it is a released version, and `OTHER` to indicate that it is just an idea or modified version.

<hr>

### Condition Expressions
- All operators:
    + `=` → Compares the equality.
    + `!=` → Compares the inequality.
    + `>` → Compares the "greater than" (for strings the string length is compared).
    + `<` → Compares the "less than" (for strings the string length is compared)
    + `<=` → Compares the "less than" OR equality (for strings, the length of the string is compared)
    + `>=` → Compares the "greater than" OR equality (for strings, the length of the string is compared)
- Condition Expressions are used to check a test
- To use this, use the `mwrite` command to write a expression
    + `mwrite @SPACE==None`
    + & Checking with `runwhen`, `runelse` or `runwhile`
        + `runwhen test.lyon`
        + `runelse falsetest.lyon`
        + `runwhile whiletest.lyon`

> © 2022 - All rights reserved<br>
> Made with ❤️ in Brazil by Marcio Dantas