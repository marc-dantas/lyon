# Lyon documentation
## Code Examples
By [@marc-dantas](https://github.com/marc-dantas)

<hr>

<h3 id="out">Example: Simple input-output</h3> 

```
var "name"
outln "--- Welcome! ---"
out "What is your name? "
readin
val "@SPACE"
loadvar "name"
outln "Hello, @SPACE!"
outln "--- Bye! ---"
```
</code></pre>

<hr>

### Example: Simple Adder

```
outln "--- Welcome! ---"
var "n1"
out "First number: "
readin 
val "@SPACE"
var "n2"
out "Second number: "
readin
val "@SPACE"
var "sum"
loadvar "n1"
sum @SPACE
loadvar "n2"
sum @SPACE
val "@NUM"
loadvar "sum"
outln "The sum is @SPACE"
```

<hr>

### Example: Running files

- main.lyon
```
outln From main.lyon!
var a
val the value from a
loadvar a
outln A = @SPACE
runfile other.lyon
```

- other.lyon
```
outln From other.lyon
var b
val the value from b
loadvar b
outln B = @SPACE
```

<hr>

### Example: Guess the number

main.lyon
```
var "guess"
readin
val "@SPACE"
loadvar "guess"
mwrite ""@SPACE"="10""
runwhen "guessed.lyon"
runelse "not_guessed.lyon"
```

guessed.lyon
```
outln "You guessed it!"
```

not_guessed.lyon
```
outln "You did not guess it!"
```

<hr>

> NOTE: Have fun with lyon!
