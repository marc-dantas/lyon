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
load_var "name"
outln "Hello, @SPACE!"
outln "--- Bye! ---"
```
</code></pre>

<hr>

### Example: Simple Adder

adder.lyon
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
load_var "n1"
sum "@SPACE"
load_var "n2"
sum "@SPACE"
val "@NUM"
load_var "sum"
outln "The sum is @SPACE"
```

<hr>

### Example: Running files

main.lyon
```
outln "From main.lyon!"
var "a"
val "The value from main"
load_var "a"
outln "A = @SPACE"
call "other.lyon"
```

other.lyon
```
outln "From other.lyon!"
var "b"
val "The value from b"
load_var "b"
outln "B = @SPACE"
```

<hr>

### Example: Guess the number

main.lyon
```
var "guess"
readin
val "@SPACE"
load_var "guess"
cmp "@SPACE"
cmp "10"
call_eq "guessed.lyon"
outln "You did not guess it!"
```

guessed.lyon
```
outln "You guessed it!"
ext
```

<hr>

### Example: Using function parameters

main.lyon
```
outln "From main.lyon function"
mem_write "Param val from main.lyon"
param_call "other.lyon"
```

other.lyon
```
outln "From other.lyon function"
```

<hr>

> NOTE: Have fun with lyon!<br>
> Goto the [docs](./index.md).

> © 2022 - All rights reserved<br>
> Made with ❤️ in Brazil by Marcio Dantas