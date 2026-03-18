# Memorization Tool

## Project description

It would be great to remember anything at any time. Alas, our mental capacity is limited. The good thing is that there are a lot of tools to help us memorize things. In this project, we are going to create a tool for memorizing lines, poems, speeches, and other text-based materials.

[View more](https://hyperskill.org/projects/159)


## Stage 1/4: Make your own flashcards

### Description

A good memorizing tool can boost your short and long-term memory. If you tried to learn a foreign language, you probably know what a flashcard is. It is an excellent device to remember facts. Flashcards alone are not enough, we need a special technique.

Let's create our flashcards first. A flashcard is a piece of paper with a question on one side and the answer on the other. Let's assume we need to memorize the capital cities of various countries. Write the country name on one side and the capital on the other.

### Objectives

In this stage, we need to create our first flashcards.
When the program starts, it should print the menu below. It is our main menu (1):
```text
1. Add flashcards
2. Practice flashcards
3. Exit
```

If `1` is entered, the program should print the following sub-menu (2):
```text
1. Add a new flashcard
2. Exit
```

By choosing the `Add a new flashcard` option, a user is prompted to enter a `Question` and an `Answer`. Once they are entered, the program automatically returns to the sub-menu (2). Iterate this process every time a user wants to add a new flashcard.

#### Flashcard practice:

The `Practice flashcards` option in the main menu (1) should print all the questions and answers that have been added previously. If there are no flashcards, print `There is no flashcard to practice!` and return to the main menu (1).

Your flashcard should appear on the screen in the following way:
```text
Question: {your question}
Please press "y" to see the answer or press "n" to skip:
```

If `y` is entered, the program should output `Answer: {your answer}` and go to the next flashcard. If there are no flashcards to show, return to the main menu (1).

If `n` is entered, skip to the next flashcard. If there are no flashcards to show, return to the main menu (1).

Once the program has reached the end of a flashcard list, return to the main menu (1).

Please keep in mind the following:

- In case of the wrong input, output the following message: `{wrong key} is not an option`. Wait for the right input.
- Your questions and answers must be non-empty values. Otherwise, wait for the input.
- Don't forget about the goodbye message. Output `Bye!` every time a user exits the program.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Brazil?
Answer:
> Brasilia

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Lebanon?
Answer:
> Beirut

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Brazil?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Brasilia

Question: What is the capital city of Lebanon?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Beirut

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Montenegro?
Answer:
> Podgorica

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Brazil?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Brasilia

Question: What is the capital city of Lebanon?
Please press "y" to see the answer or press "n" to skip:
> n


Question: What is the capital city of Montenegro?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Podgorica

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```

**Example 2:**
```text
1. Add flashcards
2. Practice flashcards
3. Exit
> 5

5 is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> we

we is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 3

3 is not an option

1. Add a new flashcard
2. Exit
> 0w

0w is not an option

1. Add a new flashcard
2. Exit
> 1

Question:
>
Question:
>
Question:
> What is the capital city of Japan?
Answer:
>

Answer:
>

Answer:
> Tokyo

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```


## Stage 2/4: Store the flashcards

### Description

In the previous stage, we created our first flashcards. The downside is that they are lost every time you close the program. We need to find a way to store them. We can use an SQLite database for this purpose. This database consists of a single file and is easy to install. To process this type of database with Python rather than SQL, we need [Object Relational Mapper (ORM)](https://en.wikipedia.org/wiki/Object-relational_mapping). SQLAlchemy can translate the Python classes to tables in relational databases and convert the function calls to SQL statements automatically.

### Theory

When establishing a connection with the database, you should add a `check_same_thread=False` flag to the database name so that Hyperskill can test your project properly
```python
engine = create_engine('sqlite:///<your database name.db>?check_same_thread=False')
```

After that, we need to create tables in the database so that the `declarative_base()` function can establish a base class. A base class stores a catalog of classes and mapped tables in the declarative system.
```python
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```

Once the base class is declared, we can define any number of mapped classes inside. For now, we want to store the answers and questions in the database. To do that we need to define the following class:
```python
from sqlalchemy import Column, Integer, String

class MyClass(Base):
    __tablename__ = 'my_table'

    id = Column(Integer, primary_key=True)
    first_column = Column(String)
    second_column = Column(String)
```

A class in declarative form must have a `__tablename__` attribute and at least one `Column` that constitutes a primary key.

We also need to call the `MetaData.create_all()` method to create the corresponding table in the database.
```python
Base.metadata.create_all(engine)
```

Now, you should create a session. And, finally, you are ready to add a new object to the table:
```python
new_data = MyClass(first_column='What is the capital city of India', second_column='New Delhi')
session.add(new_data)
session.commit()
```

The added data will be pending until we call the `commit()` method.

The `query(<mapped class name>)` method can help you access the table data.
```python
result_list = session.query(MyClass).all()
```

This code snippet above includes the `all()` method that returns a list of all added objects.
```python
print(result_list[0].question)  # What is the capital city of India
print(result_list[0].answer)    # New Delhi
print(result_list[0].id)        # 1
```

### Objectives

In this stage, your program should implement the features from Stage 1 and do the following:

1. Create a database. Please, name it `flashcard`: this will ensure the proper work of the tests (even though the tests will not check the file with the database itself).
2. Create a table in the database, name it `flashcard.db`.
3. Store a question in each table row with an answer and an ID.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Hungary?
Answer:
> Budapest

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Chile?
Answer:
> Santiago

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```

**Example 2:**
```text
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Hungary?
Please press "y" to see the answer or press 'n' to skip:
> y

Answer: Budapest

Question: What is the capital city of Chile?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Santiago

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of China?
Answer:
> Beijing

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Hungary?
Please press "y" to see the answer or press "n" to skip:
> n


Question: What is the capital city of Chile?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Santiago

Question: What is the capital city of China?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Beijing

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```

**Example 3:**
```text
1. Add flashcards
2. Practice flashcards
3. Exit
> 5

5 is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> ww

ww is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 0

0 is not an option

1. Add a new flashcard
2. Exit
> q3

q3 is not an option

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Switzerland?
Answer:
> Basel

1. Add a new flashcard
2. Exit
> 1

Question:
>
Question:
>
Question:
> What is the capital city of Australia?
Answer:
>

Answer:
>

Answer:
> Canberra

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Hungary?
Please press "y" to see the answer or press "n" to skip:
> s

Please press "y" to see the answer or press "n" to skip:
> y

Answer: Budapest

Question: What is the capital city of Chile?
Please press "y" to see the answer or press "n" to skip:
> n


Question: What is the capital city of China?
Please press "y" to see the answer or press "n" to skip:
> n


Question: What is the capital city of Swiss?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Basel

Question: what is the capital city of Australia?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Canberra

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```


## Stage 3/4: Update the flashcards

### Theory

Different Query object methods can give access to the table entries. The `all()` method returns a list of all table entries, `update({<mapped class attribute>:<new value>})` replaces the existing value with a new value, `delete()` deletes query results. Take a look at how some of the methods can be applied:
```python
entries = session.query(Database).all()  # get all table entries
entry = entries[0]

# the following lines update the entry
entry.value = 10
session.commit()

# the following lines delete the entry
session.delete(entry)
session.commit()
```

There are also such useful methods as `get(<primary key value>)` that returns an entry based on the given primary key, and `filter(<criteria>)` that returns only those entries that match the given criteria.

### Description

In this stage, we are going to add new features to our program. For example, we may need to edit or get rid of some flashcards.

### Objectives

We need to add new features to the menu that comes up once a user entered the `Practice flashcards` key from the previous stage. Let's call it the practice menu (3):
```text
press "y" to see the answer:
press "n" to skip:
press "u" to update:
```

As you can see, it still contains the `y` and `n` options. A user advances to another menu by entering `u`. Let's call it the update menu (4).
```text
press "d" to delete the flashcard:
press "e" to edit the flashcard:
```

`d` deletes a flashcard, the `e` option offers a way to edit the current flashcard. First, we need to edit the question:
```text
current question: <question>
please write a new question: 
```

Once the question has been edited, proceed to the answer:
```text
current answer: <answer>
please write a new answer:
```
If the user leaves the question or the answer field empty, keep the original question or answer value unchanged.

Output the `<wrong key> is not an option` message in both practice (3) and update (4) menus when a user presses the wrong key. Other parts of the program should operate as in the previous stages.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**
```text
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

There are no flashcards to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> Korea's capital?
Answer:
> Seoul

1. Add a new flashcard
2. Exit
> 1

Question:
> Is London England's capital?
Answer:
> Yes

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital of Ecuador?
Answer:
> Quito

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: Korea's capital?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y
Answer: Seoul

Question: Is London England's capital?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y
Answer: Yes

Question: What is the capital of Ecuador?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y
Answer: Quito

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: Korea's capital?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> u
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> e

current question: Korea's capital?
please write a new question:
> What is the capital of South Korea?

current answer: Seoul
please write a new answer:
> Seoul

Question: Is London England's capital?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> u
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> d

Question: What is the capital of Ecuador?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y
Answer: Quito

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```

**Example 2**
```text
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital of South Korea?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> r
r is not an option
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> 4
4 is not an option
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> u
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> 1
1 is not an option
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> s
s is not an option
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> d

Question: What is the capital of Ecuador?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> n

1. Add flashcards
2. Practice flashcards
3. Exit
> g

g is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```
