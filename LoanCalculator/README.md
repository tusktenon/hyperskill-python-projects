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


## Stage 2/6: Dreamworld

### Description

If you found the previous stage too easy, let's add something more interesting. The user might know the amount of the monthly payments and wonder how many months it will take to repay the loan. Let's add this functionality in addition to the calculation of the monthly payment.

In this stage, we need to ask to input the loan principal amount as before. Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. After that, the loan calculator should output the value that the user wants to know.

Also, let’s assume we don't care about decimal places. If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where you need to calculate the monthly payment. You know that the loan principal is 1000 and want to pay it back in 9 months. The real value of payment can be calculated as:

$$payment = \frac{principal}{months} = \frac{1000}{9} = 111.11...$$

Of course, you can't pay that amount of money since it's a float value. You have to round up this value and make it 112. But why do we round it up instead of rounding it down? Remember that no payment can be more than the fixed monthly payment. If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:

$$payment_{last} = principal − (periods − 1) ⋅ payment = 1000 - 8 ⋅ 112 = 104$$

In this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display the monthly payment and the last payment.

### Objectives

The behavior of your program should look like this:

- Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.
- To perform further calculations, you'll also have to ask for the required missing value.
- Finally, output the results for the user.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that this is not part of the input.

**Example 1**
```text
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
> m
Enter the monthly payment:
> 150

It will take 7 months to repay the loan
```

**Example 2**
```text
Enter the loan principal:
> 1000
What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:
> m
Enter the monthly payment:
> 1000

It will take 1 month to repay the loan
```

**Example 3**
```text
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 10

Your monthly payment = 100
```

**Example 4**
```text
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 9

Your monthly payment = 112 and the last payment = 104.
```
