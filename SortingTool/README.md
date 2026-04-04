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


## Stage 4/6: Everything counts

### Description

Now that it’s possible to sort numbers, it's time to implement the same functionality for words and lines. But that's not all for this stage! Let's also add a new sorting type that is often rather useful: sorting by count, a type of sorting that arranges the elements by number of occurrences.

Instead of `-sortIntegers`, we will use the universal `-sortingType` argument.

The result of sorting by count should be pairs `(count, dataEntry)` sorted by the `count` value.

Note that from this stage on, your program focuses on sorting user data, so it will no longer output information about the greatest number or the longest string.

### Objectives

Update the parsing of command-line arguments to support the sorting type definition:

- if the `-sortingType` argument is provided, it should be followed by `natural` or `byCount`, which defines the sorting type.
- if the argument is not provided, then consider `natural` to be the default sorting type.

Implement natural sorting for words and lines, and sorting by count for all data types. Within the group, elements with equal count values should be sorted naturally.

**Note:** for strings (words and lines), natural order is lexicographic order, for numbers it is numeric order.

Print the line containing the total number `m` of elements in the input: `Total ELEMENTS: m.`, where `ELEMENTS` can be `numbers`, `words`, or `lines`, depending on the input. Then output the sorting results:

- for natural sorting of numbers or words, print elements on one line in ascending order:
    ```text
    Sorted data: el_1 el_2 ... el_m 
    ```

- for natural sorting of lines, print lexicographically sorted elements each on a new line:
    ```text
    Sorted data:
    line_1
    line_2
    …
    line_m
    ```
    
- for sorting by count, print elements sorted by the number of occurrences, each on a new line, using the following format:
    ```text
    element: count time(s), percentage%
    ```

Here, `element` is a number, word, or line, `count` is the number of times it appears in the input, and `percentage` is the proportion of the `count` to the total number of elements in the input, given as a percentage.

### Examples

**Run configuration examples:**

```text
python main.py -sortingType natural -dataType long

python main.py -dataType word -sortingType byCount
```

**Run examples:**

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**, for sorting longs by count:
```text
> 1 -2   33 4
> 42
> 1                 1
Total numbers: 7.
-2: 1 time(s), 14%
4: 1 time(s), 14%
33: 1 time(s), 14%
42: 1 time(s), 14%
1: 3 time(s), 43%
```

**Example 2**, for sorting longs naturally:
```text
> 1 -2   33 4
> 42
> 1                 1
Total numbers: 7.
Sorted data: -2 1 1 1 4 33 42 
```

**Example 3**, for sorting words naturally:
```text
> 1 -2   33 4
> 42
> 1                 1
Total words: 7.
Sorted data: -2 1 1 1 33 4 42 
```

**Example 4**, for sorting lines naturally:
```text
> 1 -2   33 4
> 42
> 1                 1
Total lines: 3
Sorted data:
1                 1
1 -2   33 4
42
```
