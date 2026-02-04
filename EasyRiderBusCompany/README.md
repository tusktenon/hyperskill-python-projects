# Easy Rider Bus Company

## Project description

 You've just been hired by a bus company that started actively using the Internet for business. Before you came, their database had been updated a few times by various employees with various levels of skill. Your task is to find all the mistakes they made in the database. Good news: you have documentation, but bad news: it's incomplete. This promises to be quite an investigation! In this project, you will write your own programs to test data consistency and correctness. You will practice reading documentation, working with data in JSON format, and creating lists, iterators, and dictionaries. You will also learn how to work with set methods, the itertools library, and the regular expression library.

[View more](https://hyperskill.org/projects/128)


## Stage 1/6: Checking the data type

### Description

You just started sorting out the existing database of the "Easy Rider" bus company. As you take the first look at the data, you realize that it's not going to be easy.

The data that you're provided with has a lot of errors in it. Sometimes a field has no value inside it. You may notice in the example below that there are too many or too few characters in a particular field than required. Fortunately, there is documentation to help you sort out this mess. However, this documentation is not a hundred percent complete: part of it was torn away when your colleague spilled coffee on it. Let's see what we can make out.

Here are the documents that you have: [documentation](https://cogniterra.org/media/attachments/lesson/25130/Documentation.jpg) and [diagram of the bus lines](https://cogniterra.org/media/attachments/lesson/25130/Diagram_of_the_bus_line.jpg). In this stage, you will need to work with the documentation and compare the fields in the input data with the requirements specified in the **Type** and **Other** columns.

### Objectives

1. The string containing the data in JSON format is passed to standard input.
2. Check that the **data types** match.
3. Check that the **required fields** are filled in.
4. Display the information about the number of found errors in total and in each field. Keep in mind that there might be no errors at all.
5. The output should have the same formatting as shown in the example.

No need to worry about the **format (**name validation) now. In this stage, let's just make sure that the fields have the right type and all required ones are filled.

If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Note that non-required fields like `stop_type` should have the correct data type when they are not empty. Thus, for `stop_type,` which is of type Char, the field can be either empty or contain a single character (string).

### Example

Input:
```json
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
]
```

Output:
```text
Type and field validation: 8 errors
bus_id: 2
stop_id: 1
stop_name: 1
next_stop: 1
stop_type: 1
a_time: 2
```


## Stage 2/6: Correct syntax

### Description

You managed to identify the missing data and catch all the mistakes with the types. However, you noticed that there are multiple problems with suffix names for the stops: sometimes they are incorrect, and sometimes they are simply missing. As if that was not enough, you also realized that there are errors in the arrival times.

It seems like you have to carefully look at the entire **Format** column in the first part of the [documentation](https://cogniterra.org/media/attachments/lesson/25130/Documentation.jpg).

In this stage, in addition to checking the input for missing data and required types, you will also verify the suffix names for the following three fields: `stop_name`, `stop_type`, and `a_time`. As a result, sum up the errors from both type and field validations as well as format validations, and then display them together.

### Objectives

1. The string containing the data in JSON format is passed to standard input.
2. Check that the data types match and the required fields are filled in as before.
3. Count the number of format errors for `stop_name`, `stop_type`, `a_time` and merge the error counts for the relevant fields.
4. Like in the previous stage, print the information about the number of found errors in total and in each field. Remember that there might be no errors at all.
5. The output should have the same formatting as shown in the example.

If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Note that the time format is military time (24 hours, `hh:mm`). That means that there are certain restrictions:

- the first digit cannot be 3, 4, etc.;
- hours less than 10 should have zero in front of them, e.g. `08:34`;
- the delimiter should be colon `:`.

### Example

Input:
```json
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Av.",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "8:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "K",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:77"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "A",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10.12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "bourbon street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "38:13"
    },
    {
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```

Output:
```text
Type and field validation: 13 errors
bus_id: 2
stop_id: 1
stop_name: 3
next_stop: 1
stop_type: 2
a_time: 4
```


## Stage 3/6: Bus line info

### Description

It wasn't easy, but you've finally verified the data format, the required fields, and fixed all the errors in the `bus_id` field. Now, it's time to check how many bus lines we have and how many stops each line includes. Before we can go further with sorting out the database, it would be a good idea to check that the information is complete.

Here are the documents that you have: [documentation](https://cogniterra.org/media/attachments/lesson/25130/Documentation.jpg) and [diagram of the bus lines](https://cogniterra.org/media/attachments/lesson/25130/Diagram_of_the_bus_line.jpg).

### Objectives

1. The string containing the data in JSON format is passed to standard input.
2. Check the data types, required fields and format as before.
3. Find the names of all the bus lines.
4. Verify the number of stops for each line.
5. The output should have the same formatting as shown in the example.

If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

### Example

Input:
```json
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Av.",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "8:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "K",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:77"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "A",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10.12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "bourbon street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "38:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```

Output:
```text
Type and field validation: 11 errors
bus_id: 0
stop_id: 1
stop_name: 3
next_stop: 1
stop_type: 2
a_time: 4

Line names and number of stops:
bus_id: 128 stops: 4
bus_id: 256 stops: 4
bus_id: 512 stops: 2
```
