# X-mas Tree

## Project description

Welcome to a fun project that takes us back to the '80s and the world of ASCII characters. If you have ever been tasked with drawing a Christmas tree using asterisks in your programming journey, this project is for you. Drawing an entire Christmas card will make the task a bit more challenging. Get ready to have some fun!

[View more](https://hyperskill.org/projects/391)


## Stage 1/6: Reach for the stars

### Description

You have decided to write a generator of Christmas cards stylized as old graphics consisting of ASCII characters, but you have to start somewhere. Try to draw a Christmas tree consisting only of stars.

![](img/stage1a.webp)

### Objectives

1. Write a script that asks for the height of the Christmas tree Y.
2. Draw a Christmas tree with height Y.
3. The top of the Christmas tree is one character `*`.
4. Each lower level equals the higher level, with one star added to the left and one to the right.
5. The lowest possible Christmas tree will have 3 levels.
6. For a height of 3, it should look like this (the numbers on the X and Y axes are for illustrative purposes only):

    |     |  0  |  1  |  2  |  3  |  4  |
    | --- | --- | --- | --- | --- | --- |
    |  0  |     |     |  *  |     |     |
    |  1  |     |  *  |  *  |  *  |     |
    |  2  |  *  |  *  |  *  |  *  |  *  |

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:** *14 lines*

`> 14`

![](img/stage1b.webp)

**Example 2:** *7 lines*

`> 7`

![](img/stage1c.webp)


## Stage 2/4: More details

### Description

To enhance the appearance of the Christmas tree, which currently looks like a triangle made of stars, we will incorporate a few additional elements. Firstly, we will add a decorative item on the top. Secondly, we will encircle the tree with a line. And lastly, we will attach a stem at the bottom.

To make it easier, try to create a function that can insert the Christmas tree into a table of `WIDTH * HEIGHT` size, where the size of the table is equal to the width and height of the drawn Christmas tree.

### Objectives

1. Add the `X` tip to the top.
2. At the bottom, in the middle, add a stem consisting of two characters `|` separated by a space `| |`.
3. As a result, the height of the Christmas tree will be two levels higher.
4. Replace the asterisk, which has been a tip so far, with the `^` sign.
5. Replace the outermost asterisks on the left side with `/` and on the right side with `\`.
6. The tree for a height of 4 should look like this:

|     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  0  |     |     |     |  X  |     |     |     |
|  1  |     |     |     |  ^  |     |     |     |
|  2  |     |     |  /  |  *  |  \  |     |     |
|  3  |     |  /  |  *  |  *  |  *  |  \  |     |
|  4  |  /  |  *  |  *  |  *  |  *  |  *  |  \  |
|  5  |     |     | \|  |     | \|  |     |     |

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:** *14 lines*

![](img/stage2a.webp)

**Example 2:** *7 lines*

![](img/stage2b.webp)


## Stage 3/4: Christmas decorations

### Description

There's only one thing missing from the Christmas tree — decorations. We will try to place Christmas trinkets on it. But to make it more realistic, we will put them in different configurations.

### Objectives

1. In the input, in addition to the height of the Christmas tree, we also provide the interval at which the decorations appear after one space. The interval must always be greater than 0.
2. Decorations `O` can only be placed in places marked with numbers. Each subsequent level will have one more decoration. For example, let's take the height of a Christmas tree is 5.

|     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  0  |     |     |     |     |  X  |     |     |     |     |
|  1  |     |     |     |     |  ^  |     |     |     |     |
|  2  |     |     |     |  /  |  *  |  \  |     |     |     |
|  3  |     |     |  /  |  *  |  1  |  *  |  \  |     |     |
|  4  |     |  /  |  *  |  2  |  *  |  3  |  *  |  \  |     |
|  5  |  /  |  *  |  4  |  *  |  5  |  *  |  6  |  *  |  \  |
|  6  |     |     |     | \|  |     | \|  |     |     |     |

If the interval is 1, Christmas decorations should appear in all places marked with numbers:

|     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  0  |     |     |     |     |  X  |     |     |     |     |
|  1  |     |     |     |     |  ^  |     |     |     |     |
|  2  |     |     |     |  /  |  *  |  \  |     |     |     |
|  3  |     |     |  /  |  *  |  O  |  *  |  \  |     |     |
|  4  |     |  /  |  *  |  O  |  *  |  O  |  *  |  \  |     |
|  5  |  /  |  *  |  O  |  *  |  O  |  *  |  O  |  *  |  \  |
|  6  |     |     |     | \|  |     | \|  |     |     |     |

With the interval of 3, the decoration should appear every three places, in other words, in places marked 1, 4.

|     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  0  |     |     |     |     |  X  |     |     |     |     |
|  1  |     |     |     |     |  ^  |     |     |     |     |
|  2  |     |     |     |  /  |  *  |  \  |     |     |     |
|  3  |     |     |  /  |  *  |  O  |  *  |  \  |     |     |
|  4  |     |  /  |  *  |  *  |  *  |  *  |  *  |  \  |     |
|  5  |  /  |  *  |  O  |  *  |  *  |  *  |  *  |  *  |  \  |
|  6  |     |     |     | \|  |     | \|  |     |     |     |

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**

`> 14 6`

![](img/stage3a.webp)

**Example 2:**

`>7 2`

![](img/stage3b.webp)


## Stage 4/4: Let's print a postcard!

### Description

To ensure your trees are printed correctly, the first test will check if tree creation functions properly. A single tree will be printed if the input contains only two values. Otherwise, you should create a card.

### Objectives

1. The first objective is to create a postcard with width = 50 and height = 30.
2. The first and the last line contains symbols `-`.
3. Every other line starts and ends with the `|` symbol.
4. The X and Y axes position starts with 0. So, the left upper position of the symbol `-` is [0, 0], and the right bottom is [49, 29].
5. The line 27 contains the sentence `Merry Xmas` in the middle of the row.
6. The input may contain two numbers or a multiplication of four numbers.
7. If the input contains two numbers, print the Christmas tree as before. With a heigh equal to the first number and the interval of the decorations as the second number. The test checks the postcard mainly with the hash function, so it is strongly recommended to use the same function that prints the tree to use this function to put that tree on the postcard. On the other hand, the test script will not show exactly where the problem is with the tree.
8. If the input is a multiplication of four numbers, you should print a tree on the postcard in the way: `H`, `I`, `L`, `C`, where `H` is the height of the tree like before, `I` is an interval of decorations, `L` (Line) and `C` (Column) are coordinates when the top of the Christmas tree started (not the top of the tree `^` but the `X` on top). The number of trees may be higher than two.
9. The next tree printed on the postcard overlaps other trees.

The coordinates are given as shown in the figure.

![](img/stage4a.webp)

An example of an empty postcard:

![](img/stage4b.webp)

Let's consider the input `4 2 10 20 10 4 9 25`.

The first tree is drawn with a height of 4, an interval of decorations 2, and in line 10 and column 20 (coordinates [20, 10]).

![](img/stage4c.webp)

The second tree is drawn with a height of 10, an interval of decorations 4, and in line 9 and column 25 (coordinates [25, 9]). The second tree overlaps the previous one.

![](img/stage4d.webp)

### Examples

The greater-than symbol is followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**

```text
> 5 1 10 17 11 5 9 22 4 2 17 31
```

![](img/stage4e.webp)

**Example 2:**

```text
>3 2 9 31 11 3 7 25 5 1 15 35 6 3 15 15
```

![](img/stage4f.webp)
