# Lyon Documentation
By [@marc-dantas](https://gitub.com/marc-dantas)

<hr>

### All commands
- Input/Output
    + `out <value>`
    + `outln <value>`
    + `readin`
- IO Commands
    + `mem_clear`
    + `mem_write <value>`
- Variable commands
    + `clear_var`
    + `var <name>`
    + `val <value>`
    + `load_var <name>`
- Math commands
    + `clear_num`
    + `sum <number>`
    + `sub <number>`
    + `mul <number>`
    + `div <number>`
- Comparison & Flow control Commands
    + `call_ge <file>`
    + `call_le <file>`
    + `call_gt <file>`
    + `call_lt <file>`
    + `call_ne <file>`
    + `call_eq <file>`
    + `cmp <value>`
    + `clear_cmp`
- File Commands
    + `file_read <file>`
    + `file_write <file>`
- Other commands
    + `hlp`
    + `call <file>` - Call a function (file with `*.lyon` extension)
    + `param_call <file>` - Call a function (file with `*.lyon` extension) with a parameter (`@SPACE` value)
    + `typeof <value>` - Prints out the type of the value.
    + `ext` - Exit lyon

<br>

- [Input/Output](./input-output.md)
- [IO Commands](./io-commands.md)
- [Variable commands](./variable-commands.md)
- [Math commands](./math-commands.md)
- [Comparison & Flow control commands](./comparison-flow-control.md)
- [File Commands](./file-commands.md)

<hr>

### Data types
- `String`: is a sequence of characters (text) and delimited by double quotes (`"`).
- `Number`: represent a integer or a real number. (decimal cases separated by a dot (`.`))

> ***EXERCISE***: Try to use the "typeof" command (`typeof <value>`) and see the data types from diferent literals.

<hr>

### Memory
#### `@SPACE`: The space in the memory where the input and general values is stored.
- Representation: `@SPACE`
  +  Example: `setcmp "@SPACE"`
- NOTE: The default value is "None"

#### `@NUM`: The space in the memory where the numbers are stored.
- Representation: `@NUM`
    + Example: `val "@NUM"`
- NOTE: The default value is 0.

#### `@PARAM`: The space in the memory where the function parameters are stored.
- Representation: `@PARAM` 
    + Example: `sum "@PARAM"` 
- NOTE: The default value is "None".

#### `@CMP`: The space in the memory where the conditional comparisons are stored.
- NOTE: `@CMP` doesn't have a literal representation, then can't be accessed.

> ***NOTE4DEVS***: The "at" sign (@) is a convention to memory objects.

<hr>

### How lyon interpret files, commands & folders...?
lyon has a different way of interpreting files and folders, like folders being programs and files being functions. So you can use a manager to create programs (folders) that contain various functions (files).

<hr>

### Using Lyon
- To start Lyon's interactive shell, type `lyon -s`, `lyon --shell` or don't enter any parameters.
- To Start Lyon's **simple** interactive shell, type `lyon -ss` or `lyon --simple-shell`
#### Lyon Management
Lyon has a program that manages lyon programs
- To use the management mode, use `lyon -m <command>` or `lyon --manage <command>`
    + Commands
        + `new <name>` → Creates a new lyon program
        + `run <program_path>` → Runs a lyon program
        + `rundebug <program_path>` → Runs a lyon program with debug messages.
    + Program Structure (Tree)
    ```
    [program name] (folder [program])
        > src (folder)
          >> main.lyon (file [function])
          >> ... (files)
        > lyon.json (file)
    ```
- To run a single command, type `lyon -c <value>` or `lyon --command <value>`.

<hr>

### Lyon Versions
Lyon versions start at 1.0. There are three "version tags": `DEV` to indicate that it is an unreleased version, `RELEASE` to indicate that it is a released version, and `OTHER` to indicate that it is just an idea or modified version.

<hr>

> © 2022 - All rights reserved<br>
> Made with ❤️ in Brazil by Marcio Dantas