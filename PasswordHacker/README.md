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


## Stage 2/5: Simple brute force

### Description

The admin noticed someone sneaking around the site with admin rights and came up with a password. Now to log in as an admin, you need to enter the password first. Maybe the admin has set a relatively easy and short password so that it is easy to remember? Let's try to brute force all possible passwords to enter the site!

So far the program is very simplistic: it’s time to improve it so that it can generate different variants of the password and then try each one. The admin of the server doesn’t hide the information that passwords vary in length and may include letters from `a` to `z` and numbers from `0` to `9`. You should start with `a,b,c,....,z,0,1,..aa,ab,ac,ad` and continue until your password is correct. The `itertools.product()` function can help you here. It’s very important to try all the variants of every length because otherwise your program risks never finding the password!

If the password is correct, you will receive the `Connection success!` message from the server. Otherwise, you will receive the `Wrong password!` message. The server itself cannot receive more than a million attempts, so if your program works indefinitely, you will see the unfortunate message `Too many attempts`.

### Objectives

In this stage, you should write a program that:

1. Parses the command line and gets two arguments that are IP address and port.
2. Tries different passwords until it finds the correct one.
3. Prints the password it found.

Note that you only have to connect to the server once and then send messages multiple times. Don't reconnect to the server before sending every message. However, each message needs to be encoded before sending and decoded after receiving from the server.

Also, keep in mind that here and throughout the project, the password is randomly generated every time you check your code.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```text
> python hack.py localhost 9090
pass
```
