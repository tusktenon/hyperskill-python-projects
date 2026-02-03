# Arithmetic Exam Application

## Project description

Many people are fond of interactive learning. In this project, you will learn how to write an application that can facilitate solving arithmetic operations in a quick manner. The application will generate a mathematical expression for a user to solve. Implement various levels of difficulty and let the application save the results and show the progress of learning.

[View more](https://hyperskill.org/projects/173)


## Stage 1/4: Mini-calculator

### Description

People learn new things in one way or another. Learning sometimes means that you need to check your comprehension by taking a test. It also requires a person (or a program) to check your answers. You may have been in a situation when you think that you have solved the task correctly, but your professor has a different (sometimes wrong!) answer. It happens; everybody makes mistakes.

Not our application though. It should calculate the solution in a very precise manner. We need to make a simple calculator that can evaluate expressions like `a + b`, `a - b`, or `a * b`. We will leave the division aside for now.

### Objectives

1. A user inputs a line that looks like a simple mathematical operation.
2. The application should print the result of the operation.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
> 5 + 7
12
```

**Example 2:**
```text
> 3 * 100
300
```

**Example 3:**
```text
> 5 - 10
-5
```

**Example 4:**
```text
> 8 * 0
0
```


## Stage 2/4: Task generator

### Description

Any test includes at least one task. This task can vary in difficulty and required timeframes. There can be more than one task; they can demand different forms of answers. One thing remains — if there's a task, there's a solution. And we need to assess it.

Math tasks can vary in difficulty. `1 * 3` is easy. `75 * 34` is a bit more difficult. For the next stages, think about levels of difficulty that you can add!

For now, let's use random numbers from `2` to `9` and integer operations: `+`, `-` and `*`.

### Objectives

1. Generate a math task that looks like a math operation. Use the requirements above. Print it.
2. Read the answer from a user.
3. Check whether the answer is correct. Print `Right!` or `Wrong!`

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
5 * 7
> 35
Right!
```

**Example 2:**
```text
5 * 7
> 5
Wrong!
```
