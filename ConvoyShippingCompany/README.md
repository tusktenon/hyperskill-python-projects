# Convoy Shipping Company

## Project description

You're employed at "Convoy", a family transport company. Things are not going well financially, so your bosses want you to create a database to manage the company's assets in a better way and introduce scoring machines to automate some work. You will be dealing with different file formats to export data to various systems.

[View more](https://hyperskill.org/projects/151)


## Stage 1/6: Give Me an XLSX!

### Theory

In this stage, you will be dealing with an XLSX file. The Pandas library can help you convert your XLSX file to a CSV file. Use `read_excel` and `to_csv`. First, import the Pandas library:
```python
import pandas as pd
```

Then, read your XLSX file into a Pandas DataFrame object:
```python
my_df = pd.read_excel(r'File name.xlsx', sheet_name='SheetName', dtype=str)
```

The keyword argument `sheet_name` of the `read_excel` method can help you import a specific sheet from your XLSX file:
```python
sheet_name='SheetName'
```

Another keyword argument of the `read_excel` method is `dtype`. Thanks to it, the data from the table will be treated as a string and you will not encounter errors with converting Excel cells to other formats:
```python
dtype=str
```

If everything is okay, it will produce a Pandas DataFrame object filled with data. After that, you can export it to a CSV file. You can use `to_csv`, another DataFrame function, for that:
```python
my_df.to_csv(r'File name.csv')
```

There are two important attributes for this function:
```python
index=None, header=False
```

The first attribute disables numeric entry indexes in a CSV file. The second attribute prevents the function from creating additional entries at the beginning of a CSV file (in the header part).

### Description

"Convoy" experiences financial problems. You suggested making a single database that contains every company's vehicle to plan the logistics, and your management agreed. You will take a closer look at different parameters: the engine capacity, the maximum load, the fuel consumption. The data has already been collected, all you need is to output it to a CSV file.

### Objectives

1. Prompt the user to give a name for the input Excel file (complete with the .xlsx extension). For the prompt message, use `Input file name` followed by a newline.

2. Import a sheet named `Vehicles` from the entered XLSX file to a CSV file.

3. The CSV file should have the same name as the XLSX file but it should have the *.csv* extension (you can take the test table below).

4. Your program should import only the headers, omitting indexes.

5. Count the number of entries imported to the CSV file and print them out to standard output; the headers should not be counted.

6. Your program should output the following message: `X lines were imported to %file_name%.csv` or `1 line was imported to %file_name%.csv`, where `X` is the number of imported lines.
For example: `4 lines were imported to convoy.csv`

Below is an example of an XLSX table you can use. Remember that the sheet should be named `Vehicles`.

| vehicle_id | engine_capacity | fuel_consumption | maximum_load |
| ---------- | --------------- | ---------------- | ------------ |
| 2          | 200             | fuel cons. 25    | tons 14      |
| 4          | 220l            | 55               | 22           |
| n.8        | 280             | liter per km 69  | 16 ton       |
| 16         | 100             | 34l              | 24           |

You can download a sample file [here](https://cogniterra.org/media/attachments/lesson/25332/convoy.xlsx).

If you have corrupted test files, please [download them](https://cogniterra.org/media/attachments/lesson/25332/stage1_files.zip) and unzip in your working directory.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**
```text
Input file name
> convoy.xlsx
4 lines were imported to convoy.csv
```

**Example 2**
```text
Input file name
> convoy.xlsx
1 line was imported to convoy.csv
```


## Stage 2/6: Time to Clean Up CSV

### Description

As usual, no one consulted the expert (you) on how to fill the table. Another employee mixed things up and just copy-pasted entries from various documents with different formats. Luckily, no data is missing! You definitely need to clear the data from the prefixes and suffixes so that you can calculate them later. Also, you are not sure that this is the final Excel version. So, your program must include previous functionality.

### Objectives

1. Prompt the user to give a name for the input file (complete with the *.xlsx* or *.csv* extension). For the prompt message, use `Input file name` followed by a newline.

2. If your file is *.xlsx*, convert it to *.csv*.

3. If your file is *.csv* correct the data right in the file.

4. Every cell of the output file, except headers, should contain only one integer number.

5. Count the number of the cells corrected by your script.

6. Write the corrected data to a CSV file, add the `[CHECKED]` suffix to your file. For example: *%file_name%[CHECKED].csv*.

7. Your program should output the following message for the converted CSV file: `X cells were corrected` or `1 cell was corrected`, where `X` is the number of corrected cells. Include the output file name.
For example: `4 cells were corrected in %file_name%[CHECKED].csv`.

8. Display all the previous outputs for the conversions you have made earlier. 

If you have corrupted test files, please [download them](https://cogniterra.org/media/attachments/lesson/25332/stage2_files.zip) and unzip in your working directory.

### Examples

As a sample CSV test file, use your file from the first stage. Make sure that you have the cells for correction. You can also import the table provided in the first stage as an example (which covered the test cases).

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**
```text
Input file name
> data_one_xlsx.xlsx
1 line was added to data_one_xlsx.csv
4 cells were corrected in data_one_xlsx[CHECKED].csv
```

**Example 2**
```text
Input file name
> data_big_csv.csv
12 cells were corrected in data_big_csv[CHECKED].csv
```


## Stage 3/6: Finally to S3DB!

### Theory

SQLite3 is a relational database management system. You can use it for free; it is licensed as Public Domain. The system implements most SQL standards. For this project, we will use the basic SQLite3 functions.

First, import the `sqlite3` library:
```python
import sqlite3
```

To connect your database to an SQLite database, use the `connect()` method from the `sqlite3` library and create a database cursor with the `cursor()` method:
```python
conn = sqlite3.connect('%data_base_name%.s3db')
cursor_name = conn.cursor()
```

To execute an SQL query, use the `execute()` cursor method. This method will return an object that contains the result of the query. For example:
```python
result = cursor_name.execute(SQL_query_as_string)
```

To retrieve entries from the returned object, you can use two methods: `fetchall()` and `fetchone()`. The first returns all the matching entries as a list of tuples, while the second returns the next row of a query result or `None` if there are no more rows:
```python
all_rows = result.fetchall()
next_row = result.fetchone()
```

Another two important methods are `close()` and `commit()`. Remember that you need to confirm some SQL queries with the `commit` command. Otherwise, the data will be lost. At the end of your code, disconnect your database. Both methods are related to the database connection:
```python
conn.commit()
conn.closecommit()
```

If you need more information, the [SQLite Tutorial](https://www.sqlitetutorial.net/) will help you!

### Description

You are ready to create an SQLite3 database. Your bosses have some ideas on how to use the database for scoring in the future, so be ready for that! Unfortunately, it's an offer you can't refuse... The final Excel version is not ready yet. Write an algorithm that converts a corrected CSV file into an SQLite3 database.

### Objectives

1. Prompt the user to give a name for the input file (complete with the *.xlsx*, *.csv*, or *[CHECKED].csv* extension). For the prompt message, use `Input file name` followed by a newline.

2. If your file is *.xlsx* or *.csv*, perform all the previous transformations in the correct order, until you get a file that ends with *%...%[CHECKED].csv*.

3. If the file ends with *%...%[CHECKED].csv*, create an SQLite3 database with the CSV file name, change its extension to *.s3db*. Remove the *[CHECKED]* suffix. For example, *%file_name%[CHECKED].csv* should be changed to *%file_name%.s3db*.

4. Use *"convoy"* as the name for your database table.

5. Use headers from the CSV file as the names of the table columns.

6. The `vehicle_id` column should have the `INTEGER` type; make sure it's `PRIMARY KEY`.

7. Other columns should have the `INTEGER` type with `NOT NULL` attributes.

8. Insert the entries from your *%...%[CHECKED].csv* file.

9. Count the number of entries inserted into the database.

10. Your program should output the following message: `X records were inserted` or `1 record was inserted`, where `X` is a number of inserted records and the output file name.
For example: `4 records were inserted into %file_name%.s3db`.

11. Display all the previous outputs for the conversions you have made.

In case of unexpected errors, the test scripts may not be able to remove `.s3db` files from previous tests. To avoid exceptions we suggest deleting previous files before creating new ones.

If you have corrupted test files, please [download them](https://cogniterra.org/media/attachments/lesson/25332/stage3_files.zip) and unzip in your working directory.

### Examples

You can use the *%...%[CHECKED].csv* test file from the previous stage.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**
```text
Input file name
> data_one_xlsx.xlsx
1 line was added to data_one_xlsx.csv
4 cells were corrected in data_one_xlsx[CHECKED].csv
1 record was inserted into data_one_xlsx.s3db
```

**Example 2**
```text
Input file name
> data_big_csv.csv
12 cells were corrected in data_big_csv[CHECKED].csv
10 records were inserted into data_big_csv.s3db
```

**Example 3**
```text
Input file name
> data_big_chk[CHECKED].csv
10 records were inserted into data_big_chk.s3db
```
