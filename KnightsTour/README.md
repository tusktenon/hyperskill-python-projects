# Knight's Tour Puzzle

## Project description

The Knight’s Tour is a fun puzzle where you move the knight so that it visits every square of the chessboard once. The rules are simple and fun, but the game is really hard to master. Let’s make a program to find a solution! This project will help you practice concepts frequently tested in technical interviews at top tech companies.

[View more](https://hyperskill.org/projects/141)


## Stage 1/6: Setting up the board

### Description

The knight's tour problem uses a chessboard and a knight. Don't worry, you won't need to know the chess basics for this project, you only need to know how a knight moves on the board.

A standard chess board is an 8x8 square on which the chess pieces are placed. For this project, we will use a coordinate system (x,y) to label each square on the chessboard, where (1,1) is the bottom left, and (8,8) is the top right.

![](img/coordinates.webp)

The knight is a chess piece. It moves in an L-shape and can jump over other pieces. It has to move 2 squares horizontally and 1 square vertically, or 2 squares vertically and 1 square horizontally.

![](img/movements.webp)

The rules of the knight's tour are as follows:

- The knight can start at any square.
- The knight must visit every square by moving in the L-shape.
- The knight can visit each square only once.
- The knight can finish anywhere on the board. This is called an 'open' tour of the board.
- You win if you visit every square on the board.
- You lose if you fail to visit every square only once without revisiting it.

### Objectives

Let's get started by setting up the puzzle:

1. Ask the user for the knight's starting position.
2. If the user input contains non-integer numbers you should print `Invalid dimensions!`.
3. If the user input contains more than 2 numbers you should print `Invalid dimensions!`.
4. If the user input numbers out of bounds of the game field you should print `Invalid dimensions!`.
5. Display the 8x8 chessboard with the knight in this position. You should display a frame around the board and mark the column and row numbers. You should use an underscore `_` for an empty cell with a space in between them, and an `X` for the knight's position.

### Example

The greater-than symbol followed by space (`> `) represents the user input. Note that it's not part of the input.
```text
Enter the knight's starting position: > 1 3
 -------------------
8| _ _ _ _ _ _ _ _ |
7| _ _ _ _ _ _ _ _ |
6| _ _ _ _ _ _ _ _ |
5| _ _ _ _ _ _ _ _ |
4| _ _ _ _ _ _ _ _ |
3| X _ _ _ _ _ _ _ |
2| _ _ _ _ _ _ _ _ |
1| _ _ _ _ _ _ _ _ |
 -------------------
   1 2 3 4 5 6 7 8 
```
