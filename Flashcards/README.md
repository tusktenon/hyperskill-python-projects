# Flashcards

## Project description

When learning a new language, it can be hard to remember all the new vocabulary, which is exactly where flashcards can help. Typically, flashcards show a hint (a task or a picture) on one side and the right answer on the other. Flashcards can be used to remember any sort of data, so if you want to create a useful tool to help your learning and your programming skills, this project is for you. You will practice concepts frequently tested in technical interviews at top tech companies.

[View more](https://hyperskill.org/projects/127)


## Stage 1/7: Stage one, card one

### Description

A flashcard is a digital or paper card that contains a term on one side, and a definition, translation, or explanation of that term on the other. Flashcards are often used for learning foreign languages and are an effective study technique for many people.

![An example of a flashcard. The upper part is the term the user is being asked, the lower part is the correct answer. Source: [Wikipedia](https://en.wikipedia.org/wiki/Flashcard).](Example.gif)

For this project, we’ll refer to the text on the front of the card as the term, and the text on the back will be the definition. There won't actually be any visual "front" and "back" side of a card: it'll all be done through sequential text. We'll ask the user for the definitions of the terms they previously entered, and check whether the given answers are correct. While developing this application, you will not only learn some programming but also save paper!

### Objectives

Your program should read two lines from the console, a term, and a definition, that represent a card.

Implement a program that outputs 4 lines:

- The first line is `Card:`
- The second line is the term provided by the user
- The third line is `Definition:`
- The fourth line is the definition which is also provided by the user

In this stage we are just laying the foundation for later stages, we'll start using these input values from next stage.

### Examples

Here are some output examples to clarify what the result should look like. The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1.**
```text
Card:
> purchase
purchase
Definition:
> buy
buy
```

**Example 2.**
```text
Card:
> cos'(x)
cos'(x)
Definition:
> -sin(x)
-sin(x)
```


## Stage 2/7: What's on the card?

### Description

In Stage 1, we learnt how to create a dynamic flashcard from user's input. Let’s add a primitive guessing mechanism as well so that the user can check how well they remember the definitions.

For this stage you'll extend the flashcard-creation mechanism implemented in Stage 1 and add a functionality to check the user's answer on top of it.

### Objectives

Similar to Stage 1, your program should read two lines from the console, a *term*, and a *definition*, that represent a card. However there's no need to print `Card:` or `Definition:` in this stage.

After that, the user inputs a line as an *answer* (a definition of the term on the card). Compare the user's answer with the correct definition and print the result.

The output of the program must be one of the following:

- `Your answer is wrong...` if the answer doesn't match the definition;
- `Your answer is right!` if the answer matches the definition.

Of course, at this point, the user is unlikely to get the answer wrong, since they’re the ones who just typed in the answer... But don’t worry: right now we're just warming up so that in later stages we could make this a bit more challenging for our users.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:** *the user's answer is correct*

Input (a term, a definition, an answer):
```text
> print()
> outputs text
> outputs text
```

Output:
```text
Your answer is right!
```

**Example 2:** *the user's answer is incorrect*

Input (a term, a definition, an answer):
```text
> Jetbrains
> A place for people who love to code
> A place for people who hate to code
```

Output:
```text
Your answer is wrong...
```
