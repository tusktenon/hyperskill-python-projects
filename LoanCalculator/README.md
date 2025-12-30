# Loan Calculator

## Project Description

Personal finance can be tricky, but it doesn't have to be! This project helps you understand loans and mortgages with a handy calculator. Just provide a few details like loan amount, interest rate, and payment terms. The program will calculate key financial parameters, making informed decisions easier. You can determine your monthly payment, the total interest paid, or the loan amount you can afford. Plus, it's a great way to understand the command-line interface. So, ditch those complex spreadsheets and let our calculator simplify your finances, one calculation at a time. Get ready to become your own financial guru!

[View more](https://hyperskill.org/projects/90)


## Stage 1/6: Beginning

### Description

Let's think about what a loan calculator should be able to do. In general, it takes several parameters like a loan principal and interest, calculates the values the user wants to know (for example, monthly payment or overpayment), and outputs them to the user.

Not familiar with these concepts? Don't worry, we will explain them to you in simple terms. The principal is the original amount of money you borrow. The interest is a charge for borrowing that money, usually calculated as a percentage of the principal amount.

### Objectives

Let's start by imitating this behavior:

- Prompt the user to enter their loan principal.
- Prompt the user to enter their monthly payment.
- Calculate and display the number of months required to repay the loan by dividing the loan principal by the monthly payment.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that this is not part of the input.
```text
Enter the loan principal:
> 1000
Enter the monthly payment:
> 200

It will take 5 months to repay the loan
```
