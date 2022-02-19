# Lyon documentation
## Flow Control
By [@marc-dantas](https://github.com/marc-dantas)

<hr>

### Commands
- `call_ge <file>` [here](#call_ge)
- `call_le <file>` [here](#call_le)
- `call_gt <file>` [here](#call_gt)
- `call_lt <file>` [here](#call_lt)
- `call_ne <file>` [here](#call_ne)
- `call_eq <file>` [here](#call_eq)
- `cmp <value>` [here](#cmp)
- `clear_cmp` [here](#clear_cmp)

<hr>

<h3 id="cmp">Command: <code>cmp</code></h3> 

- Set a comparison value to the comparison space in the memory (only two values)
- Syntax: `cmp <value>`

<hr>

<h3 id="clear_cmp">Command: <code>clear_cmp</code></h3>

- Clear the comparison space in the memory.
- Syntax: `clear_cmp`

<hr>

<h3 id="call_eq">Command: <code>call_eq</code></h3>

- Call a function if the comparison (equality from the comparison values in the memory) is true.
- Syntax: `call_eq <file>`

<hr>

<h3 id="call_ne">Command: <code>callne</code></h3>

- Call a function if the comparison (difference from the comparison values in the memory) is true.
- Syntax: `call_ne <file>`

<hr>

<h3 id="call_lt">Command: <code>call_lt</code></h3>

- Call a function if the comparison ("less than" from the comparison values in the memory) is true.
- Syntax: `call_lt <file>`

<hr>

<h3 id="call_le">Command: <code>call_le</code></h3>

- Call a function if the comparison ("less than OR equality" from the comparison values in the memory) is true.
- Syntax: `call_le <file>`

<hr>

<h3 id="call_gt">Command: <code>call_gt</code></h3>

- Call a function if the comparison ("greater than" from the comparison values in the memory) is true.
- Syntax: `call_gt <file>`

<hr>

<h3 id="call_ge">Command: <code>callge</code></h3>

- Call a function if the comparison ("greater than OR equality" from the comparison values in the memory) is true.
- Syntax: `call_ge <file>`

<hr>

> © 2022 - All rights reserved<br>
> Made with ❤️ in Brazil by Marcio Dantas