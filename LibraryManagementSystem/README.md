# Library Management System

## Project description

Good library management is all about keeping records. In the past, special logbooks were reserved for these purposes. The modern solution are databases, an excellent tool for storing big chunks of information — anything, from images to text, single-character data to thousands of digits. You don't even need to keep this data on your computer! Let's see how databases can help you with running a library.

[View more](https://hyperskill.org/projects/272)


## Stage 1/4: Create a table

### Description

We need to store a lot of information in the library database: return dates, members' names, books available, and much more. For this purpose, we should create tables and match their columns with the correct data types. Let's get started!

### Objectives

Take a look at the database outline below.

![](database.svg)

The table `book` contains information about all the books in the library: title, author's name, genre, number of pages and year of publication, rating, and how many books are available.

The `student` and `staff` tables include information about the employees who issue books and readers.

The `operation` table includes information about transactions that have occurred: who issued the book and to whom, and the date of issue (`iss_date`), as well as the planned return date (`return_date`) and the return indicator (`return_indicator`, issued — `0`, returned — `1`).

Your task is to create tables, set the data types for the columns, and apply the SQL constraints.

Pay attention to the following:

- Don’t forget to highlight the primary key and foreign key features. On the scheme, they are marked in bold and connected with lines.
- Restrict the columns to `NOT NULL`.
- You do not have to worry about generating unique identifiers for rows within a table if its primary key column is declared as `INTEGER PRIMARY KEY`.

Use the SQLite syntax for creating tables. The following links could help you to find more information on data types and foreign key in SQLite: [Datatypes in SQLite](https://www.sqlite.org/datatype3.html), [Foreign Key Support](https://www.sqlite.org/foreignkeys.html).

### Example

Assign your queries to the variables, as in the example. It is required for testing only.

**Example 1:** *an extract from the program*
```text
create_book_table = "CREATE TABLE book (
   id INTEGER PRIMARY KEY,
   ...
   ...
);"

create_student_table = "CREATE TABLE student (
   id INTEGER PRIMARY KEY,
   ...
   ...
);"
```


## Stage 2/4: Staff and books

### Description

You have created the necessary tables, but these tables should not remain empty. The library never stops working — readers take and return books every day. Large libraries need long shelves and databases for dealing with massive pools of data. It's time to fill our tables!

### Objectives

Add the following data requested from you to the required tables:

- The `book` table:

| book_name                                 | isbn       | genre         | author       | book_year | book_count | book_page | rank |
| ----------------------------------------- | ---------- | ------------- | ------------ | --------- | ---------- | --------- | ---- |
| The Metamorphosis                         | 0393347095 | Novella       | Franz Kafka  | 2014      | 2          | 128       | 4.4  |
| Harry Potter And The Order Of The Phoenix | 0439358078 | Fantasy       | J.K. Rowling | 2004      | 3          | 896       | 4.2  |
| Anna Karenina                             | 0198800533 | Realist Novel | Leo Tolstoy  | 2017      | 1          | 896       | 4.6  |

- The `staff` table:

| full_name     | gender | date_of_birth |
| ------------- | ------ | ------------- |
| Steve Smith   | Male   | 1992-04-23    |
| Ashley Miller | Female | 1995-01-16    |

- The `student` table:

| full_name      | gender | date_of_birth |
| -------------- | ------ | ------------- |
| Mia Yang       | Female | 1996-09-15    |
| Bob Lee        | Male   | 1997-12-13    |
| Eric Rampy     | Male   | 1995-08-21    |
| Stefany Ferenz | Female | 1996-04-01    |

- The `operation` table:

| student_id | staff_id | book_id | iss_date   | return_date   | return_indicator |
| ---------- | -------- | ------- | ---------- | ------------- | ---------------- |
| 3          | 1        | 1       | 4 days ago | 10 days later | False            |
| 1          | 1        | 3       | Yesterday  | 13 days later | False            |
| 2          | 2        | 2       | Yesterday  | 6 days later  | False            |
| 4          | 2        | 2       | Today      | 14 days later | False            |

Pay attention to the following:

- Calculate the `iss_date` and `return_date` values.
- You may either write a date as a string in the following format `YYYY-MM-DD` or use the `date()` function to calculate a date. For example, `date('now')` will return the current date. Check out [this link](https://www.sqlite.org/lang_datefunc.html) for more details.
- For `return_indicator` with delivery information: `0` = `False`, `1` = `True`.

### Example

Do not delete the code you've composed in the previous stage. Assign your queries to the variables, as in the example. It is required for testing only.

**Example 1:** *an extract from the program*
```text
insert_book_table = "INSERT INTO book VALUES (...);"

insert_staff_table = "INSERT INTO staff VALUES (...);"
```


## Stage 3/4: Remove old books

### Description

Sometimes, there's a need to change the number of books or return dates. A member can take more than one book; damaged books should be discarded. For these changes, update the database regularly.

### Objectives

Let's see what our data looks like now:

- The `book` table:

| id  | book_name                                 | isbn       | genre         | author       | book_year | book_count | book_page | rank |
| --- | ----------------------------------------- | ---------- | ------------- | ------------ | --------- | ---------- | --------- | ---- |
| 1   | The Metamorphosis                         | 0393347095 | Novella       | Franz Kafka  | 2014      | 2          | 128       | 4.4  |
| 2   | Harry Potter And The Order Of The Phoenix | 0439358078 | Fantasy       | J.K. Rowling | 2004      | 3          | 896       | 4.2  |
| 3   | Anna Karenina                             | 0198800533 | Realist Novel | Leo Tolstoy  | 2017      | 1          | 896       | 4.6  |

- The `staff` table:

| id  | full_name     | gender | date_of_birth |
| --- | ------------- | ------ | ------------- |
| 1   | Steve Smith   | Male   | 1992-04-23    |
| 2   | Ashley Miller | Female | 1995-01-16    |

- The `student` table:

| id  | full_name      | gender | date_of_birth |
| --- | -------------- | ------ | ------------- |
| 1   | Mia Yang       | Female | 1996-09-15    |
| 2   | Bob Lee        | Male   | 1997-12-13    |
| 3   | Eric Rampy     | Male   | 1995-08-21    |
| 4   | Stefany Ferenz | Female | 1996-04-01    |

- The `operation` table:

| student_id | staff_id | book_id | iss_date   | return_date   | return_indicator |
| ---------- | -------- | ------- | ---------- | ------------- | ---------------- |
| 3          | 1        | 1       | 4 days ago | 10 days later | False            |
| 1          | 1        | 3       | Yesterday  | 13 days later | False            |
| 2          | 2        | 2       | Yesterday  | 6 days later  | False            |
| 4          | 2        | 2       | Today      | 14 days later | False            |

In this stage, update the following:

- Replace the following information with what exists in the table: `Ashley Miller` -> `Ashley Bailey`;
- `Eric Rampy` returned the book ten days before the return date. Make the necessary changes to the operation table: change the return date and the returned column to `true` for transaction;
- Add one more book to the available "The Metamorphosis" accordingly.

### Example

Do not delete the code you've composed in the previous stage. Assign your queries to the variables, as in the example. It is required for testing only.

**Example 1:** *an extract from the program*
```text
update_staff_inf = "UPDATE staff SET ... ;"

update_operation_inf = "UPDATE operation SET ...;"

update_book_inf = "UPDATE book SET ... ;"
```

## Stage 4/4: Verify data

### Description

In a real library, hundreds of students borrow hundreds of different books every day. By combining different tables, we can solve all kinds of problems that arise. For example, having received a fresh sequel of "Harry Potter", we can easily choose exactly those students who are most likely to be interested in it and offer it to them.

### Objectives

Let's remember what our database looks like:

![](database.svg)

Write a query where we can find the names of the students who bought the book with `id = 2`. The results should be sorted by `full_name`, and you should build your query using the JOIN keyword.

### Example

Do not delete the code you've composed in the previous stage. Assign your queries to the variables, as in the example. It is required for testing only.

**Example 1:** *an extract from the program*
```text
student_inf = "SELECT full_name FROM ... ;"
```
