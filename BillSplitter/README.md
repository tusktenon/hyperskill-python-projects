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


## Stage 2/4: The bill has arrived

### Description

It's bill time! Let's split the bill among everyone and update the values in the dictionary you have created in the previous stage.

Since we don't want to deal with too many decimals (who carries that much change anyway?), round the split amount to two decimal places and then update the dictionary with the split values.

### Objectives

In this stage your program should perform the following steps together with the steps of the previous stage:

1. If there are no people to split the bill (the number of friends is 0 or an invalid input), output `"No one is joining for the party"`;
2. Else, take user input: the final bill;
3. Split the total bill equally among everyone;
4. Round the split value to two decimal places;
5. Update the dictionary with the split values;
6. Print the updated dictionary.

Do not print the output of the previous stage (see examples).

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:** *Five people joining*
```text
Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
```

**Example 2:** *Seven people joining*
```text
Enter the number of friends joining (including you):
> 7

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason
> Ben
> Ned

Enter the total bill value:
> 41

{'Marc': 5.86, 'Jem': 5.86, 'Monica':5.86, 'Anna': 5.86, 'Jason': 5.86, 'Ben': 5.86, 'Ned': 5.86}
```

**Example 3:** *Invalid input*
```text
Enter the number of friends joining (including you):
> 0

No one is joining for the party
```
