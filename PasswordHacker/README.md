# Password Hacker

## Project description

All sorts of creatures lurk around the Internet, including trolls, pirates, miners – and hackers. In this project, you're going to step into the shoes of a hacker, tasked with infiltrating a secret server — password unknown. Your mission is to create a Python program that can crack the password swiftly. Learn how hacking works and create a complex application where you will work on iterators and generators, itertools and time module. You will practice concepts frequently tested in technical interviews at top tech companies.

[View more](https://hyperskill.org/projects/80)


## Stage 1/5: Establishing a connection

### Description

Imagine some admin who runs a website on the Internet. The site is becoming very popular, and a lot of people register. Filling in their profiles, they leave some information there that is not meant to be public, for example, information about their credit cards.

The admin completely forgot about the security of the site, so now you can log in with admin privileges without even having a login and password!

> [!NOTE]
> Terms like "hacking" and "hacker" are frequently associated with negativity. However, in this project, we will be operating as White Hats. Throughout all stages, simulated scenarios will be employed. Remember, any skills and knowledge acquired during this project should be used exclusively for ethical and educational purposes. Still, it is possible that publishing your work on this project may be viewed ambiguously by platforms or employers. We recommend caution to avoid being flagged or banned.

The first task of this project is to go to the admin's site; it will immediately give out all the secret information. Remember, as soon as you enter the site as an admin, you will automatically obtain all the private data of the site. It will get harder: the tasks of all other stages of the project will be to crack the admin password. Good luck!

Your program should connect to the server using an IP address and a port from the command line arguments. You can use socket module to create this program.

### Objectives

Your program will receive command line arguments in this order:

1. IP address
2. port
3. message for sending

The algorithm is the following:

1. Create a new socket.
2. Connect to a host and a port using the socket.
3. Send a message from the third command line argument to the host using the socket.
4. Receive the server’s response.
5. Print the server’s response.
6. Close the socket.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
> python hack.py localhost 9090 password
Wrong password!
```

**Example 2:**
```text
> python hack.py 127.0.0.1 9090 qwerty
Connection Success!
```
