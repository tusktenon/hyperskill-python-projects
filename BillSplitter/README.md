# Bill Splitter

## Project description

Eating out with friends is fun, but splitting the bill can be tricky. This project helps you develop a Python-based tool to easily divide restaurant bills equally. Input the number of friends and the total bill amount, and the app calculates each person's share. No more awkward calculations or uneven splits!

[View more](https://hyperskill.org/projects/175)


## Stage 1/4: Invite your friends

### Description

You have planned a dinner with your friends today. It's the right time to add them to your program. You need to be sure how many friends are joining you for dinner including you.

The idea is to take names from user input. Store them in a dictionary.

For example, if five friends are joining including you, you need to add five people to the dictionary so that you can access/update the corresponding bill value later.

### Objectives

In this stage your program should perform the following steps:

1. Take user input — how many people want to join, including the user;
2. In case of an invalid number of people (zero or negative), "No one is joining for the party" is expected as an output;
3. Otherwise, take the friends' names as input, iteratively;
4. Store them in a dictionary initialized with zeros;
5. Print out the dictionary.

To communicate with the user, you can use the prompts specified in the examples.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:** *Valid input*
```text
Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

{'Marc': 0, 'Jem': 0, 'Monica': 0, 'Anna': 0, 'Jason': 0}
```

**Example 2:** *Invalid input*
```text
Enter the number of friends joining (including you):
> 0

No one is joining for the party
```

**Example 3:** *Invalid input*
```text
Enter the number of friends joining (including you):
> -1

No one is joining for the party
```
