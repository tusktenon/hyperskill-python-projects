# University Admission Procedure

It takes a lot of hard work to enroll in the university of your dreams. Although, we tend to dismiss how difficult it is for the university to handle the document volume. In this project, you'll deal with university applicants. You'll implement an algorithm to determine which applicants are going to be enrolled. At each stage, the algorithm will gradually become more complex and comprehensive! You will practice concepts frequently tested in technical interviews at top tech companies.

[View more](https://hyperskill.org/projects/163)


## Stage 1/7: No one is left behind!

### Description

Let's create a program that will help the university determine the best candidates for enrolling!

The first step is very simple. An applicant needs to take three exams and submit the scores. The score of an exam can vary from 0 to 100. Your program should read the numbers representing the exam scores, calculate the mean exam score, and output it. Finally, enroll the applicant to the university, as there are no other contestants yet.

### Objectives

At this stage, your program should:

1. Take three inputs as integer numbers. They are the exam results.
2. Calculate the mean score of all three numbers. If the mean is a fractional number, don't discard the fractional part.
3. Print the resulting number.
4. Print the `Congratulations, you are accepted!` line.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```text
> 75
> 90
> 68
77.66666666666667
Congratulations, you are accepted!
```


## Stage 2/7: Raising the bar

### Description

It'd be great if universities could enroll everybody, but it's not very realistic, is it? Let's refine our algorithm. In this stage, we need to set a threshold of the mean score — if the mean score of the applicant is equal to or greater than `60.0`, the program should notify the applicant of their acceptance to the university. Otherwise, inform them about their rejection.

### Objectives

At this stage, your program should:

1. Read the numbers and output the mean score, as in the previous stage.
2. If the mean score is equal to or greater than `60.0`, output the following message: `Congratulations, you are accepted!`
3. If the mean score is less than `60.0`, output the following message: `We regret to inform you that we will not be able to offer you admission.`

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:** *the applicant is enrolled*
```text
> 70
> 56
> 81
69.0
Congratulations, you are accepted!
```

**Example 2:** *the applicant is rejected*
```text
> 100
> 43
> 27
56.666666666666664
We regret to inform you that we will not be able to offer you admission.
```


## Stage 3/7: Going big

### Description

Things are heating up! Our university has become trendy, so the applicants are rushing in. Your program has to be adapted to this — unfortunately, we cannot enroll everybody. The program will need to rank the potential students and determine who's going to get admitted. At this stage, you'll need to work with the Grade Point Average (GPA). It is the mean grade of all high school courses. We don't need the threshold, for now, a certain number of applicants with the best GPA will be accepted instead.

### Theory

To proceed further we need to understand the basics of sorting. To use more than one attribute for list sorting, use the following syntax:
```python
not_sorted_list = [['c', 11], ['a', 11], ['c', 10]]
sorted_list = sorted(not_sorted_list, key=lambda x: (x[0], x[1]))
print(sorted_list)
# [['a', 11], ['c', 10], ['c', 11]]
```

In this example, the first value (`x[0]`) of each element of the `not_sorted_list` is used for sorting in the first place. If these values are equal, the second value (`x[1]`) is used to determine which element is greater.

A problem may occur if you want to sort the list in ascending order by the first value and in descending order by the second value. For example, you have two values to sort the list by: score and time.
```python
# the first element in each nested list is score
# the second element is time
not_sorted_list = [[531, 11.76], [401, 5.11], [531, 10.05]]
```

You want to sort your list in such a way that the elements with the highest score and the smallest time value would go before the elements with a lower score and greater time value. To do this, you can simply inverse one of the values by adding a minus in front of it:
```python
# both lines will lead to the same result
sorted_list = sorted(not_sorted_list, key=lambda x: (-x[0], x[1]))
sorted_list = sorted(not_sorted_list, reverse=True, key=lambda x: (x[0], -x[1]))
print(sorted_list)
# [[531, 10.05], [531, 11.76], [401, 5.11]]
```

### Objectives

At this stage, your program should:

1. Read the first input, an **N** integer representing the total number of applicants.
2. Read the second input, an **M** integer representing the number of applicants that should be accepted to the university.
3. Read **N** lines from the input. Each line contains the first name, the last name, and the applicant's GPA. These values are separated by one whitespace character. A GPA is a floating-point number with two decimals.
4. Output the `Successful applicants:` message.
5. Output **M** lines for applicants with the top-ranking GPAs. Each line should contain the first and the last name of the applicant separated by a whitespace character. Successful applicants' names should be printed in descending order depending on the GPA — first, the applicant with the best GPA, then the second-best, and so on.
6. If two applicants have the same GPA, rank them in alphabetical order using their full names (we know it's not really fair to choose students by their names, but what choice do we have?)

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
> 5
> 3
> Cole Collins 3.68
> Dolores Baldwin 3.40
> Brett Boyer 2.45
> Nora Alston 3.71
> Jessy Moore 3.14
Successful applicants:
Nora Alston
Cole Collins
Dolores Baldwin
```

**Example 2:** *applicants with equal GPA, note that the full name is used to sort these applicants*
```text
> 3
> 2
> Albert Collins 3.02
> Albert Nelson 3.02
> Cole Allen 3.02
Successful applicants:
Albert Collins
Albert Nelson
```
