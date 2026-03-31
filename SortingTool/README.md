# Sorting Tool with Python

## Project description

In the modern world, data has become so abundant that processing it is no easy business. How can anyone make sense of all those words and numbers? In this project, you will write a program that processes textual and numeric data and sorts it. Your program will be able to determine the largest or most frequent pieces of data and perform the necessary calculations on them. You will practice concepts frequently tested in technical interviews at top tech companies. Data is waiting to be sorted!

[View more](https://hyperskill.org/projects/307)


## Stage 1/6: Numbers only

### Description

With this project, you will learn how to process numeric and text input, sort it, and output useful information about the data. Your final program will work with numbers, words, and lines. In the first stage, we will stick to integer numbers.

The program should read user input consisting of several lines, each containing integers separated by an arbitrary number of spaces. Then it should count the number of integers in the input, find the greatest one, and identify the number of times this integer appears. Finally, it should print this information to the console.

If you run your program and try to type in the numbers manually, you'll see that this process will go on infinitely. To end the input, the user should type the [end-of-file](https://en.wikipedia.org/wiki/End-of-file) symbol, informing the operating system that no more input will be provided. On Linux and Mac, the shortcut for this symbol is Ctrl+D or Cmd+D, and on Windows the combination is Ctrl+Z. To check for the end-of-file symbols in your program, use the following construction:
```python
while True:
    try:
        data = input()
    except EOFError:
        break
```
This will break the while loop if the end of the input is reached.

### Objectives

Read integers from the console until the end of the input is reached.

Compute the following information:

1. The number of integers in the input (X)
2. The greatest number in the input (Y)
3. How many times the greatest number occurs in the input (Z)

Output it using this template:
```text
Total numbers: X.
The greatest number: Y (Z time(s)).
```

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```text
> 1 -2   33 4
> 42
> 1                 1
Total numbers: 7.
The greatest number: 42 (1 time(s)).
```
