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

<hr>

<h3 id="outln">Example: Running files</h3>

- main.lyon
```
outln From main.lyon!
var a
val the value from a
ldvar a
outln A = $SPACE
runfile other.lyon
```

- other.lyon
```
outln From other.lyon
var b
val the value from b
ldvar b
outln B = $SPACE
```

<hr>

> NOTE: Have fun with lyon!
