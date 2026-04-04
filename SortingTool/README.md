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


## Stage 2/6: Not just numbers

### Description

Remember how we wanted the program to work not only with numbers but also with lines and words? In this stage, you will add behavior for text data types to your program. You will also implement parsing for command-line arguments that will allow the user to define the input data type

After parsing the arguments and reading the input, the program should treat the input according to its data type and output an information message similar to the one from the previous stage.

### Objectives

1. Parse arguments that define the input data type:
    - if the optional `-dataType` argument is provided, it should be followed by `long`, `line`, or `word`, which means that the input consists of numbers, lines, or words, respectively.
    - if the argument is not provided, you should assume that the `-dataType` argument is `word`.

2. Read the input depending on the type:
    - `long` — numbers with an arbitrary number of spaces between them, just like in the previous stage.
    - `line` — each line treated as a whole string.
    - `word` — continuous sequences of characters separated by an arbitrary number of spaces.

3. Compute the following information about the data:
    1. The number of lines, numbers, or words in the input.
    2. The greatest number or the longest line or word in the input.
    3. How many times this greatest or longest element occurs in the input (compare words and lines by length; if two elements are the same length, arrange them alphabetically).
    4. The greatest/longest element's occurrence percentage.

4. Print this information as shown in the examples. Note that percentage should be printed as integer value and the longest line should be printed on a separate line, so you will end up printing 4 lines instead of 2.

### Examples

**Run configuration examples:**
```text
python main.py -dataType long

python main.py -dataType line

python main.py -dataType word
```

**Run examples**

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1,** for integers:
```text
> 1 -2   333 4
> 42
> 1                 1
Total numbers: 7.
The greatest number: 333 (1 time(s), 14%).
```

**Example 2,** for lines:
```text
> 1 -2   333 4
> 42
> 1                 1
Total lines: 3.
The longest line:
1                 1
(1 time(s), 33%).
```

**Example 3,** for words:
```text
> 1 -2   333 4
> 42
> 1                 1
Total words: 7.
The longest word: 333 (1 time(s), 14%).
```


## Stage 3/6: Sorting it out

### Description

This project is called Sorting Tool, but, so far, you still haven’t really sorted the elements of the user input. Let's add a number-sorting mechanism to the program and provide an appropriate command-line argument to use this function.

The new optional `-sortIntegers` argument indicates that the input numbers should be sorted.

### Objectives

Update the parsing of command-line arguments to support the number sorting option.

If the `-sortIntegers` argument is provided, ignore the other arguments and output two lines: the first containing the total number of numbers in the input, and the second containing all of the input numbers in ascending order.

If the `-sortIntegers` argument is not provided, the behavior of the program should be the same as in the previous stage.

### Example

**Run configuration example:**
```text
python main.py -sortIntegers
```

**Run example**
The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```text
> 1 -2   33 4
> 42
> 1                 1
Total numbers: 7.
Sorted data: -2 1 1 1 4 33 42
```
