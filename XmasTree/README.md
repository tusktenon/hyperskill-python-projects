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
