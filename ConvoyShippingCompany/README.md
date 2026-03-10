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
