# Examples

Here are some examples of SimpleFast code to give you a taste of what the language looks like and what you can do with it.

## Hello, World!

Here's the traditional "Hello, World!" program in SimpleFast:

```simplefast
print 'Hello, World!'
```

## Variables and Arithmetic

This example demonstrates variable assignment and basic arithmetic operations:

```simplefast
let x be 10
let y be 20
let sum be x + y
print 'The sum is: {sum}'
```

## Functions

This is how you define and call a function in SimpleFast:

```simplefast
define function add with parameters x, y:
    return x + y
end function

let sum be add 10, 20
print 'The sum is: {sum}'
```

## Classes and Objects

Here's an example of defining a class and creating an object:

```simplefast
define class Point with properties x, y:

    define constructor with parameters x, y:
        this.x be x
        this.y be y
    end constructor

    define method distance_from_origin:
        return (this.x ^ 2 + this.y ^ 2) ^ 0.5
    end method

end class

let p be new Point 3, 4
print 'Distance from origin: {p.distance_from_origin}'
```

## Asynchronous I/O

Here's an example of how you might perform asynchronous I/O in SimpleFast:

```simplefast
import iolib  # This is a hypothetical I/O library for SimpleFast.

define async function read_file with parameters filename:
    let file be await iolib.open_file filename, 'r'
    let contents be await file.read
    await file.close
    return contents
end function

let contents be await read_file 'myfile.txt'
print 'File contents: {contents}'
```

These examples should give you a sense of the simplicity and expressiveness of SimpleFast. For a more comprehensive introduction to the language, check out the tutorial in the `docs` directory.
