# Calculator for Investors

## Project description

Create a small program that helps investors make a fundamental analysis based on the company's reports and estimate the company's performance. With this calculator, you can choose the best company in the industry and decide whether to buy its shares or not.

[View more](https://hyperskill.org/projects/264)


## Stage 1/4: What's on the menu?

### Description

Create a menu for your program and ask users what to do. If users select to end the program, quit with a farewell message.

### Objectives

Let's break the task into several steps:

- Create the `MAIN MENU`, `CRUD MENU`, and the `TOP TEN MENU`;
- Display the `MAIN MENU`;
- Ask for an option: `Enter an option:`;
- Display the selected menu;
- Ask for an option: `Enter an option:`;
- When a valid option is selected, print `Not implemented!`;
- When an invalid option is selected, print `Invalid option!`;
- Quit with a farewell message: `Have a nice day!`;

The code snippets below show the menus:

```text
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria
```

```text
CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies
```

```text
TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA
```

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> one
Invalid option!

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 99
Invalid option!

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 0
Have a nice day!
```

**Example 2:**
```text
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 1

CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies

Enter an option:
> 1
Not implemented!

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 1

CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies

Enter an option:
> 4
Not implemented!

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 0
Have a nice day!
```

**Example 3:**
```text
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 2

TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA

Enter an option:
> 1
Not implemented!

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 0
Have a nice day!
```


## Stage 2/4: Store it

### Description

A **database** is an organized collection of data, typically stored electronically in a computer system.

Let's create a database. In this stage, your program will read the files and create a database with them. Follow the objectives and examples to improve your program.

[companies.csv](https://cogniterra.org/media/attachments/lesson/26667/companies.csv)

[financial.csv](https://cogniterra.org/media/attachments/lesson/26667/financial.csv)

### Objectives

Let's break the task into several steps:

- Read the data from *test/companies.csv* and *test/financial.csv*;
- Replace the empty values with `None`;
- Create an SQLite database — *investor.db*;
- Create the `companies` table;
- Create the `financial` table;
- Insert datasets to the tables;
- End the program with a message: `Database created successfully!`;

The snippet below shows the detail of the `companies` model. Please don't change the terms and types.
```text
ticker: String, primary_key
name: String
sector: String
```

The snippet below shows the details of the `financial` model. Please don't change the terms and types.
```text
ticker: String, primary_key
ebitda: Float
sales: Float
net_profit: Float
market_price: Float
net_debt: Float
assets: Float
equity: Float
cash_equivalents: Float
liabilities: Float
```

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```text
Database created successfully!
```
