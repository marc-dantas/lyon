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
val @SPACE
ldvar name
outln Hello, @SPACE!
outln --- Bye! ---
```
</code></pre>

<hr>

### Example: Simple Adder

```
outln --- Welcome! ---
var n1
outln First number: 
rdin 
val @SPACE
var n2
outln Second number:
rdin
val @SPACE
var sum
ldvar n1
sum @SPACE
ldvar n2
sum @SPACE
val $NUM
ldvar sum
outln The sum is @SPACE
```

<hr>

### Example: Running files

- main.lyon
```
outln From main.lyon!
var a
val the value from a
ldvar a
outln A = @SPACE
runfile other.lyon
```

- other.lyon
```
outln From other.lyon
var b
val the value from b
ldvar b
outln B = @SPACE
```

<hr>

### Example: Guess the number

main.lyon
```
var guess
rdin
val @SPACE
ldvar guess
iowrt @SPACE=10
runif guessed.lyon
runelse not_guessed.lyon
```

guessed.lyon
```
outln You guessed it!
```

not_guessed.lyon
```
outln You did not guess it!
```

<hr>

> NOTE: Have fun with lyon!
