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
ldvar name
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
ldvar n1
sum $SPACE
ldvar n2
sum $SPACE
val $NUM
ldvar sum
outln The sum is $SPACE
```

> NOTE: Have fun with lyon!