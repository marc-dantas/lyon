# Lyon documentation
## Code Examples
By [@marc-dantas](https://github.com/marc-dantas)

<hr>

<h3 id="out">Example: Simple input-output</h3> 

```
var name
outln --- Welcome! ---
outln What is your name?
rdin
val $SPACE
outln Hello, $SPACE!
outln --- Bye! ---
```
</code></pre>

<hr>

<h3 id="outln">Example: Simple Adder</h3>

```
outln --- Welcome! ---
var n1
outln First number:
rdin
val $SPACE
var n2
outln Second number:
rdin
val $SPACE
var sum
load n1
add $SPACE
load n2
add $SPACE
val $NUM
load sum
outln The sum is $SPACE
```
<hr>

<h3 id="rdin">Command: <code>rdin</code></h3>

- Reads a value from the console and stores it in `SPACE` space in the memory.
- Syntax: `rdin`