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
# Machine Learning and Deep Learning Examples

Here's how you might implement some machine learning and deep learning tasks in SimpleFast. 
These examples assume the existence of a hypothetical machine learning library named `mlib` and a deep learning library named `dlib`.

## Linear Regression

Here's an example of training a simple linear regression model:

```simplefast
import mlib

define function train_model with parameters X, y:
    let model be new mlib.LinearRegression
    model.fit X, y
    return model
end function

let X be [[1], [2], [3], [4], [5]]
let y be [2, 4, 6, 8, 10]
let model be train_model X, y

let prediction be model.predict [[6]]
print 'Prediction for input 6: {prediction}'
```

## Neural Network

Here's an example of defining and training a simple neural network for a classification task:

```simplefast
import dlib

define function train_model with parameters X, y:
    let model be new dlib.Sequential
    model.add new dlib.Dense 64, 'relu', input_shape=[X.shape[1]]
    model.add new dlib.Dense 32, 'relu'
    model.add new dlib.Dense 10, 'softmax'  # Assume we have 10 classes

    model.compile 'categorical_crossentropy', optimizer='adam', metrics=['accuracy']

    model.fit X, y, epochs=10, batch_size=32
    return model
end function

# Assume X_train and y_train are your training data and labels
let model be train_model X_train, y_train

let prediction be model.predict X_test  # Assume X_test is your test data
print 'Prediction: {prediction}'
```

These examples should give you a sense of how SimpleFast can be used for machine learning and deep learning tasks. For more detailed guides and tutorials, check out the `mlib` and `dlib` documentation in the `docs` directory.


These examples should give you a sense of the simplicity and expressiveness of SimpleFast. For a more comprehensive introduction to the language, check out the tutorial in the `docs` directory.


