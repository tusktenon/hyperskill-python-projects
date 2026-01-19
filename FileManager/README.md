# File Manager

## Project description

We bet you know how to rename, copy, and delete files on your computer, but have you ever considered creating your file manager? This project will help you do just that. You can guide your file helper through folders, check sizes, and edit content. It's a must-have tool for organizing your computer.

[View more](https://hyperskill.org/projects/378)


## Stage 1/5: Set the working directory

### Description

We know you know what a file manager is. Remember Windows Explorer? You can view files and folders in a directory and navigate between folders using icons or by entering a directory path.

Our file manager will do the same things, but with one exception: it'll be a text-based manager, not a visual one. You'll control the manager with text commands instead of clicking on icons and interacting with menus — *so old school*.

Let's start with implementing the navigation feature. It enables us to go from one directory to another. In the later stages, we can perform some actions on files within these directories.

Your file manager should be able to execute the following commands:

- `pwd` tells you in which directory you currently are
- `cd` changes the current directory 

Moreover, the `cd` command can have the following attributes to specify in which directory the file manager should move to:

- `cd C:\folder1\folder2` moves from the current directory to the directory with the absolute path of *C:\folder1\folder2*. In other words, after this command is entered, the current directory should be changed to *folder2* located on disk *C:* inside *folder1*;

- `cd ..` moves one directory up. That is if the current directory is *C:\folder1\folder2*, the current directory is changed to *C:\folder1*;

- `cd folder2` (when the user is in *C:\folder1*) moves to the relative file path. The current directory should be changed to *C:\folder1\folder2*.

### Objectives

In this stage, your program should:

1. Print the prompt message: `Input the command`

2. Take the command from the user.

    - If the command is `pwd`, print the absolute path of the current directory.
    Note: The starting directory is the one where your file manager program is located. For example, if your file manager program has an absolute path *C:\Users\user\Projects\FileManager\manager.py*, and the first user command is `pwd`, the file manager should print `C:\Users\user\Projects\FileManager`.

    - If the command is `cd ..`, move one level up from your current directory. Print the name of the new current folder.

    - If the command is `cd path\path\path` (that is, `cd` with a relative folder path), move to the folder specified by the user. Print the name of the new current folder.

    - If the user inputs any other command (including `cd` with no arguments), print the error message: `Invalid command`.

    - In case the specified file or directory does not exist, handle the error using `FileNotFoundError` and print an error message of your choice. After the error message, the program should ask for input again.

3. Keep on taking new commands from the user until they type `quit`. If the user types `quit`, quit the program. 

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
Input the command
> pwd
C:\Users\User\PycharmProjects\File Manager
> cd ..
PycharmProjects
> pwd
C:\Users\User\PycharmProjects
> cd ..
User
> pwd
C:\Users\User
> cd C:\Users\Documents
Documents
> cd C:\Users\Documents\Report
Report
> cd ..
Documents
> cd
Invalid command
> ppp
Invalid command
> pwd
C:\Users\Documents
> quit
```


## Stage 2/5: What do we have here?

### Description

The previous stage was a good start. However, we need directories to store something... and there is not much use in browsing them when you can't even see their content. Let's fix that.

In this stage, we will implement a new command to get quick info about the state of the current directory. The name of the command is `ls`. The user can use `ls` in three different ways:

- `ls` prints the list of files and subdirectories in the current directory.
- `ls -l` prints the list of subdirectories and the list of files, and for each file, it specifies its size in bytes.
- `ls -lh` outputs the size of files in a human-readable format. The size of each file can be indicated not only in bytes but also in kilobytes, megabytes, or gigabytes. This way, it'll be much more convenient to read the list of files and find the largest one in the folder, in case you need that!

### Objectives

In this stage, your program should:

- Support all the commands from the previous stage. The interaction between the user and the program remains the same: the user inputs a command, the program outputs the result, accepts a new command, and so on.
- Provide a new command — `ls` . If the user inputs `ls` without arguments, print the list of subdirectories and files in the current directory.
    - The program should print the names of the files together with extensions. For example, `test.txt` (instead of just `test`)
    - The list of subdirectories should precede the list of files.
    - The order of items in these lists is irrelevant.
    - The program shouldn't output anything if there are no files and subdirectories.
- If the user inputs `ls -l`, the program should output the same lists. However, the list of files should also contain the size of each file **in bytes**. This information can be found via `os.stat(filename).st_size`. The name of the file and its size should be separated by one space character.
- If the user inputs `ls -lh`, the program should output the same lists together with the sizes of the files. However, the size should be printed in human-readable format:
    - the size should be converted to bytes, kilobytes, megabytes, or gigabytes, depending on the file size. Then, the converted size and the unit should be printed. For example, `100MB` or `1GB`.
    See the table below for details:

| Size of the file                        | Output format | Example of the output |
| ----------------------------------------| ------------- | --------------------- |
| < 1024 bytes (< 1 KB)                   | `<size>B`     | `608B`, `900B`        |
| 1 KB (1024 B) <= size < 1 MB (1024 KB)  | `<size>KB`    | `600KB`               |
| 1 MB (1024 KB) <= size < 1 GB (1024 MB) | `<size>MB`    | `550MB`               |
| >= 1 GB (1024 MB)                       | `<size>GB`    | `2GB`                 |

Note that the number of bytes, kilobytes, megabytes, and gigabytes should be integer. If the calculated size of the file is not an integer, round it to the nearest integer.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
Input the command
> pwd
C:\Users\User
> cd ..
Users
> ls
User
mouse.jpg
> cd User
User
> pwd
C:\Users\User
> quit
```

**Example 2:**
```text
Input the command
> pwd
C:\Users\User\PycharmProjects\File Manager
> cd ..
PycharmProjects
> ls
Hangman
Search Engine
Spell Checker
test.txt
readme.md
image.png
> ls -l
Hangman
Search Engine
Spell Checker
test.txt 47302
image.png 5767168
movie.mp4 2684354560
> ls -lh
Hangman
Search Engine
Spell Checker
test.txt 46KB
image.png 5MB
movie.mp4 2GB
> cd Hangman
Hangman
> ls -l
readme.md 0
> ls -lh
readme.md 0B
> quit
```


## Stage 3/5: Cleaning time

### Description

We can now inspect the content of any directory. Our program lists all files in the directory by command and specifies their size. We can use that to find the largest file in the directory, for example, and get rid of it to clean up some space. But wait, our file manager doesn't know how to do it yet.

Well, not for long. In this stage, we'll teach our file handler a few new tricks:

- `rm` deletes a specified file or a directory;
- `mv` renames any file or directory;
- `mkdir` creates a new directory.

In this stage, our file manager will start correcting user mistakes. For example, if the user wants to remove a file that doesn't exist, the file manager should notify them about that and cancel the execution of the command.

### Objectives

In this stage, your file manager should:

- Support all the commands from the previous stage;

- Support the new `rm` command:

    - The command deletes a file or a folder

    - The user should specify the path to the file or the folder meant to be deleted. For example: `rm C:\Users\Alex\Documents\test.txt` or `rm D:\Photos`

    - The user doesn't have to specify the absolute path to the file or folder. They can specify a relative path as they did with `cd` in the previous step. For example, `rm test.txt` will remove `test.txt` from the current directory. In this case, the current directory is the starting point for the relative path. If the current directory is `C:\Users`, and the user inputs `rm test.txt`, the file manager should delete the file that's located at `C:\Users\test.txt`.

    - If the user didn't specify any file or folder name, the file manager should output `Specify the file or directory`

    - If the user inputs the name of a file or folder that doesn't exist, output `No such file or directory`

- Support the new `mv` command:

    - The command renames a file or folder

    - The user should specify the name of the file or folder to be renamed and the new desired name. For example, `mv old_name.txt new_name.txt`.

    - For now, let's only support renaming the files that are located in the current directory

    - If the user didn't specify exactly two names in the command, output `Specify the current name of the file or directory and the new name`

    - If the user wants to rename a file or folder that doesn't exist, output `No such file or directory`

    - If there's already a file or folder with the same name as was specified in the user's input, output `The file or directory already exists`. If on Unix and using `os.rename`, you may need to check if the input file exists first because the file will be renamed without raising an exception if the program has the necessary permissions.

- Support the new `mkdir` command:

    - The command creates a new folder

    - If the user didn't specify a folder name, output an error message `Specify the name of the directory to be made`

    - The user should specify the absolute or relative path of the new directory, for example: `mkdir D:\Projects\NewProject` or `mkdir NewProject`.

    - If such a directory already exists, output an error message `The directory already exists`

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:** *removing directories*
```text
Input the command
> pwd
D:\PyCharmProjects
> ls
Hangman
Search Engine
readme.txt
> rm Hanhman
No such file or directory
> rm Hangman
> ls
Search Engine
readme.txt
> rm
Specify the file or directory
> rm Search Engine
> ls
readme.txt
> quit
```

**Example 2:** *renaming a file*
```text
Input the command
> pwd
E:\SecretFolder
> ls
VerySecret
very_personal_image.jpg
> mv image.jpg random.jpg
No such file or directory
> mv very_personal_image.jpg ordinary_image.jpg
> ls
VerySecret
ordinary_image.jpg
> quit
```

**Example 3:** *creating a new directory*
```text
Input the command
> pwd
E:\SecretFolder
> cd E:\SecretFolder\VerySecret
> ls
VeryVerySecret
> mkdir
Specify the name of the directory to be made
> mkdir VeryVerySecret
The directory already exists
> ls
VeryVerySecret
> mkdir VerySecret_2
> ls
VerySecret_2
VeryVerySecret
> quit
```


## Stage 4/5: Copy-paste

### Description

Removing files and directories will allow us to empty some space. But sometimes, we delete things that we should have kept safe. Before we increase the scale of our work, let's make some commands that can copy files and move them to other directories.

For safekeeping:

- `cp` copies a file and saves that copy in a new directory
- `mv` now, additionally, can move a file to a new directory

### Objectives

In this stage, your file manager should:

- Support all the commands from the previous stage.

- Support the new `cp` command:

    - This command copies a file.

    - The user should specify the paths. For example, `cp C:\Users\Alex\Documents\test.txt C:\Users` to copy the file from the `Documents` folder and place that copy in the `Users` folder;

    - The user doesn't have to specify the absolute path to the file or folder. They can use a relative path. If the current working directory is `C:\Users`, and the user inputs the command `cp test.txt Alex`, the file manager should copy the file `C:\Users\test.txt` and save that copy in `C:\Users\Alex`;

    - If the user didn't specify any file, the file manager should output the message: `Specify the file`;

    - If the user inputs the name of a file or folder that doesn't exist, output the message: `No such file or directory`;

    - If the user specified more than two names in the command, output a message: `Specify the current name of the file or directory and the new location and/or name`;

    - If the destination location already has a file with that name, for example, `cp Alex\test.txt Alex`, do not copy it. Instead, output the message: `{filename} already exists in this directory`.

- Expand the functionality of the `mv` command:

    - This command can rename or move a file;

    - The user can specify absolute or relative paths, as described in `cp` above;

    - If the user specifies a path, move the file to that new location. For example, `mv test.txt Alex` will move `test.txt` from the current directory to the subdirectory `Alex`.

    - If the user specifies a different filename for the target folder, move the file to the target folder and rename the file to that different filename. For example, `mv Alex\text.txt Alex\Documents\lorem_ipsum.txt` will remove `text.txt` from the `Alex` directory and put it into the `Alex\Documents` directory with the new name `lorem_ipsum.txt`;

    - If the user didn't specify exactly two names in the command, output a message: `Specify the current name of the file or directory and the new location and/or name`;

    - If the destination location already has a file with that name, do not move the file. Instead, output the message: `The file or directory already exists`.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:** *copying a file*
```text
Input the command
> pwd
C:\Users\Cheryl
> ls
Backup
test.txt
> cp test.txt Backup
> ls
Backup
test.txt
> cd Backup
Backup
> ls
test.txt
> quit
```

**Example 2:** *moving a file*
```text
Input the command
> pwd
C:\Users\User\Games
> ls
Project1
Project2
Trash
> cd Project2
Project2
> ls
game.exe
crashlog.txt
> mv crashlog.txt C:Users\User\Games\Trash
crashlog.txt already exists in this directory
> mv crashlog.txt C:Users\User\Games\Trash\crashlog2.txt
> cd ..
Games
> cd Trash
Trash
>ls
crashlog.txt
crashlog2.txt
> rm crashlog.txt
> rm crashlog2.txt
> quit
```

**Example 3:** *a variety of commands*
```text
Input the command
> pwd
D:\PyCharmProjects
> ls
Hangman
Search Engine
readme.txt
> cp readme.txt Hangman
> ls
Hangman
Search Engine
readme.txt
> cd D:\PycharmProjects\Hangman
Hangman
> ls
readme.txt
> cp readme.txt ..
readme.txt already exists in this directory
> rm readme.txt
> cd ..
PycharmProjects
>mv readme.txt Hangman\hreadme.txt
ls
Hangman
Search Engine
> cd D:\PycharmProjects\Hangman
Hangman
> ls
hreadme.txt
> quit
```


## Stage 5/5: Mass migration

### Description

Our file manager has basic functionality, including navigation, viewing file sizes, renaming files and folders, moving files, and copying files. However, it can be time-consuming to act on individual files, such as deleting 1000 text files while leaving 80 image files untouched. To address this, we can add name templates to our manager for more efficient large-scale work.

The premise is simple. Instead of operating on a single file, the user can input a file extension (for example, .txt), and the file manager will act on every file with that extension in the current working directory.

### Objectives

In this stage, your file manager should:

- Support all the commands from the previous stage;

- Accept the `rm` command along with a file extension. Delete all files with that file extension in the current working directory. For example, `rm .txt` will delete all files of *.txt* type in the current working directory.

    - If the user inputs the name of a file type that doesn't exist in the current working directory, the file manager should output the message: `File extension {extension} not found in this directory`.

- Accept the `cp` command along with a file extension. Copy all files with that extension in the current working directory to a target directory.

    - If the user inputs the name of a file extension that doesn't exist in the current working directory, the file manager should output the message: `File extension {extension} not found in this directory`;

    - If the destination location already has a file with that name, halt the process, and output the prompt: `{filename} already exists in this directory. Replace? (y/n)` and take input from the user. If the user inputs `y`, replace the file in the destination folder with the new one. If the user inputs `n`, do not copy this file over; instead, move on to the next file(s) to be copied. If the user inputs anything else, repeat the question.

- Update the `mv` command to move all files with that file extension in the current working directory to a target directory if a file extension is input. Do not also update the `mv` renaming feature to work with file extensions.

    - If the user inputs the name of a file extension that doesn't exist in the current working directory, the file manager should output the message: `File extension {extension} not found in this directory`;

    - If the destination location already has a file with that name, halt the process and output the prompt: `{filename} already exists in this directory. Replace? (y/n)` and take input from the user. If the user inputs `y`, replace the file in the destination folder with the new file. If the user inputs `n`, do not copy this file over. Instead, move on to the next file(s) to be copied. If the user inputs anything else, repeat the question.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:** *removing all files of a given file extension via rm*
```text
Input the command
> pwd
C:\Users\Cheryl
> ls
Backup
test.txt
test1.txt
test2.txt
seminar_notes.txt
ascii_art_texture_practice.txt
> rm .txt
> ls
Backup
> rm .txt
File extension .txt not found in this directory
> rm .jpg
File extension .jpg not found in this directory
> rm .bats
File extension .bats not found in this directory
> quit
```

**Example 2:** *copying all files of a given file extension via cp*
```text
Input the command
> pwd
C:\Users\Cheryl
> ls
Backup
test.txt
> cd Backup
Backup
> ls
test.txt
test1.txt
test2.txt
seminar_notes.txt
ascii_art_texture_practice.txt
> cp .tx ..
File extension .tx not found in this directory
> cp .txt ..
test.txt already exists in this directory. Replace? (y/n)
> y
> ls
test.txt
test1.txt
test2.txt
seminar_notes.txt
ascii_art_texture_practice.txt
> cd ..
Cheryl
> ls
Backup
test.txt
test1.txt
test2.txt
seminar_notes.txt
ascii_art_texture_practice.txt
> quit
```

**Example 3:** *moving all files of a given extension via mv*
```text
Input the command
> pwd
C:\Users\Cheryl\Backup
> ls
> cd ..
Cheryl
> ls
Backup
test.txt
test1.txt
test2.txt
seminar_notes.txt
ascii_art_texture_practice.txt
> mv .txt Backup
> ls
Backup
> cd Backup
Backup
> ls
test.txt
test1.txt
test2.txt
seminar_notes.txt
ascii_art_texture_practice.txt
> quit
```
