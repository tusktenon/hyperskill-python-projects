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


## Stage 4/6: One Part to JSON...

### Description

Your database is ready. As you may have expected, you still don't have the final Excel version. Your boss told you that you will have to export part of the database to two different systems. You don't know which data goes where, but rumor has it you will need a scoring function for this. For now, your algorithm should export all the database entries. The first system needs the data in the JSON format.

### Objectives

1. Prompt the user to give a name for the input file (complete with the *.xlsx*, *.csv*, *[CHECKED].csv* or *.s3db* extension). For the prompt message, use `Input file name` followed by a newline.

2. If your file is *.xlsx* or *.csv*, or it ends with the *%...%[CHECKED].csv*, perform all previous transformations in the correct order until you get an SQLite3 file.

3. Once you have an SQLite3 file, generate a JSON file with the same name; use the *.json* extension.

4. The JSON object should have the following structure ( the indenting is for illustration purposes only and doesn’t need to appear in the output file):
    ```json
    {
        "convoy": [
            {
                "vehicle_id": 2,
                "engine_capacity": 200,
                "fuel_consumption": 25,
                "maximum_load": 70
            },
            {
                "vehicle_id": 1024,
                "engine_capacity": 500,
                "fuel_consumption": 80,
                "maximum_load": 150
            }
        ]
    }
    ```

5. Save the data to a file as a JSON object .

6. Count the number of entries exported to the JSON file.

7. Your program should output the following message: `X vehicles were saved` or `1 vehicle was saved`, where `X` is a number of inserted entries. It should also include the output file name.
For example: `10 vehicles were saved into %file_name%.json`.

8. Display all the previous outputs for the conversions you have made.

If you have corrupted test files, please [download them](https://cogniterra.org/media/attachments/lesson/25332/stage4_files.zip) and unzip in your working directory.

### Examples

You can use the *.s3db* test file from the previous stage as a sample.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**
```text
Input file name
> data_one_xlsx.xlsx
1 line was added to data_one_xlsx.csv
4 cells were corrected in data_one_xlsx[CHECKED].csv
1 record was inserted into data_one_xlsx.s3db
1 vehicle was saved into data_one_xlsx.json
```

**Example 2**
```text
Input file name
> data_big_csv.csv
12 cells were corrected in data_big_csv[CHECKED].csv
10 records were inserted into data_big_csv.s3db
10 vehicles were saved into data_big_csv.json
```

**Example 3**
```text
Input file name
> data_big_chk[CHECKED].csv
10 records were inserted into data_big_chk.s3db
10 vehicles were saved into data_big_chk.json
```
**Example 4**
```text
Input file name
> data_one_sql.s3db
1 vehicle was saved into data_one_sql.json
```


## Stage 5/6: ...Another to XML

### Description

It's time to make the final transformation. You need to convert your SQLite3 database to XML. In this stage, your algorithm should export all the database entries. The final Excel file is expected next week: they promised.

### Objectives

1. Prompt the user to give a name for the input file (complete with the *.xlsx*, *.csv*, *[CHECKED].csv* or *.s3db* extension). For the prompt message, use `Input file name` followed by a newline.

2. If your file is *.xlsx* or *.csv*, or it ends with *%...%[CHECKED].csv*, perform all the previous transformations in the correct order until you get an SQLite3 file.

3. If your file is *.s3db*, generate a fresh JSON file, and XML with the same name, and the extensions *.json* and *.xml*. Both files should have all the entries from the SQLite3 file.

4. An XML file with two entries should look like this:
    ```xml
    <convoy>
        <vehicle>
            <vehicle_id>2</vehicle_id>
            <engine_capacity>200</engine_capacity>
            <fuel_consumption>25</fuel_consumption>
            <maximum_load>70</maximum_load>
        </vehicle>
        <vehicle>
            <vehicle_id>4</vehicle_id>
            <engine_capacity>220</engine_capacity>
            <fuel_consumption>55</fuel_consumption>
            <maximum_load>110</maximum_load>
        </vehicle>
    </convoy>
    ```
5. Indentation size is not important.

6. A number is located between the tags with no spaces.

7. Save the data to the XML file. It can be either a single string or a formatted block of text as in the example above.

8. Count the number of entries exported to the XML file.

9. Your program should output the following message: `X vehicles were saved` or `1 vehicle was saved`, where `X` is the number of inserted entries. It should include the output file name.
For example: `10 vehicles were saved into file_name.xml`.

10. Display all the previous outputs for the conversions you have made.

If you have corrupted test files, please [download them](https://cogniterra.org/media/attachments/lesson/25332/stage5_files.zip) and unzip in your working directory.

### Examples

You can use the *.s3db* test file from stage 3.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**
```text
Input file name
> data_one_xlsx.xlsx
1 line was added to data_one_xlsx.csv
4 cells were corrected in data_one_xlsx[CHECKED].csv
1 record was inserted into data_one_xlsx.s3db
1 vehicle was saved into data_one_xlsx.json
1 vehicle was saved into data_one_xlsx.xml
```

**Example 2**
```text
Input file name
> data_big_csv.csv
12 cells were corrected in data_big_csv[CHECKED].csv
10 records were inserted into data_big_csv.s3db
10 vehilces were saved into data_big_csv.json
10 vehicles were saved into data_big_csv.xml
```

**Example 3**
```text
Input file name
> data_big_chk[CHECKED].csv
10 records were inserted into data_big_chk.s3db
10 vehicles were saved into data_big_chk.json
10 vehicles were saved into data_big_chk.xml
```

**Example 4**
```text
Input file name
> data_one_sql.s3db
1 vehicle was saved into data_one_sql.json
1 vehicle was saved into data_one_sql.xml
```


## Stage 6/6: It's Scoring Time!

### Description

The requirements for the scoring function have been defined. And it looks like you have the final version of the Excel file. It's time to prepare the scoring function and export the selected entries to JSON and XML files.

The idea of scoring function is to define under what conditions the scoring points are to be given. The next step is to determine how many points are enough to qualify or reject the testing object.

In our case, the management clarified some key issues:
1) Number of pitstops. If there are two or more gas stops on the way, the object has 0 points. One stop at the filling station means 1 point. No stops — 2 scoring points.
2) Fuel consumed over the entire trip. If a truck burned 230 liters or less, 2 points are given. If more — 1 point.
3) Truck capacity. If the capacity is 20 tones or more, it gets 2 points. If less — 0 points.

It was found that the average route length is 450 km. Do not include the return path: 450 kilometers is the whole route. Remember that the `engine_capacity` is in liters, the `fuel_consumption` is in liters/100 kilometers, and the `maximum_load` is in tonnes.

Interesting fact: scoring functions are often used by banks to pre-estimate the so-called credit score.

### Objectives

1. Prompt the user to give a name for the input file (complete with the *.xlsx*, *.csv*, *[CHECKED].csv* or *.s3db* extension). For the prompt message, use `Input file name` followed by a newline.

2. If your file is *.xlsx* or *.csv*, or it ends with *%...%[CHECKED].csv*, perform all the previous transformations in the correct order.

3. Add the `score` column to *.s3db* files. Populate the column with the scoring points, according to the algorithm described above. The `score` column should be added during the conversion from *%...%[CHECKED].csv* to *.s3db*.

4. Generate JSON and XML files according to the scoring points. All entries with a score of greater than 3 should be exported to the JSON file, others to the XML file.

5. The `score` column should not be exported to JSON and XML files.

6. Count the number of entries imported to JSON and XML files.

7. Your program should output the following message: `X vehicles were saved` or `1 vehicle was saved`, where `X` is the number of inserted entries. The program should include the output file name. For example:
    ```text
    9 vehicles were saved into %file_name%.json
    0 vehicles were saved into %file_name%.xml
    ```

8. Display all the previous outputs for the conversions you have made.

For example, take a look at the following entries:

| vehicle_id | engine_capacity | fuel_consumption | maximum_load |
| ---------- | --------------- | ---------------- | ------------ |
| 10         | 200             | 50               | 6            |

In the SQLite database, they should look like this:

| vehicle_id | engine_capacity | fuel_consumption | maximum_load | score |
| ---------- | --------------- | ---------------- | ------------ | ----- |
| 10         | 200             | 50               | 6            | 3     |

Route length is 450 km. One stop at the filling station (1 point), the fuel consumption is below 230 liters (2 points), and the maximum capacity is below 20 tonnes (0 points). This entry should go to the XML file.

If you have corrupted test files, please [download them](https://cogniterra.org/media/attachments/lesson/25332/stage6_files.zip) and unzip in your working directory.

### Examples

You can use the files from the previous stages.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**
```text
Input file name
> data_final_xlsx.xlsx
19 lines were added to data_final_xlsx.csv
3 cells were corrected in data_final_xlsx[CHECKED].csv
19 records were inserted into data_final_xlsx.s3db
12 vehicles were saved into data_final_xlsx.json
7 vehicles were saved into data_final_xlsx.xml
```

**Example 2**
```text
Input file name
> data_big_csv.csv
12 cells were corrected in data_big_csv[CHECKED].csv
10 records were inserted into data_big_csv.s3db
7 vehicles were saved into data_big_csv.json
3 vehicles were saved into data_big_csv.xml
```

**Example 3**
```text
Input file name
> data_big_chk[CHECKED].csv
10 records were inserted into data_big_chk.s3db
7 vehicles were saved into data_big_chk.json
3 vehicles were saved into data_big_chk.xml
```

**Example 4**
```text
Input file name
> data_big_sql.s3db
10 vehicles were saved into data_big_sql.json
0 vehicles were saved into data_big_sql.xml
```
