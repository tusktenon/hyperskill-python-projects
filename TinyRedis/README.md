# Tiny Redis

## Project description

Ever wondered how Redis, one of the world's most popular in-memory databases, works under the hood? Redis powers the backend infrastructure of countless applications - from caching user sessions in social media platforms to managing real-time leaderboards in gaming applications, storing shopping carts in e-commerce systems, and enabling instant messaging in chat applications. In this comprehensive project, you'll build your own simplified Redis server from scratch, tackling the real-world problem of efficient data storage and retrieval that every high-traffic application faces. This project is perfect for backend developers who want to deepen their understanding of network programming and concurrent systems. After completing this project, you will be able to add it to your portfolio as your own full-scale in-memory database!

[View more](https://hyperskill.org/projects/549)


## Stage 1/6: Simple TCP server

### Description

Welcome to the first stage of our Tiny Redis implementation. At the end of this project, you will have a working in-memory database compatible with the [Redis Serialization Protocol](https://redis.io/docs/latest/develop/reference/protocol-spec/).

**Why would you even want an in-memory database?** Think of it like this: there are documents that you need to permanently store somewhere in a big file cabinet and access them once in a while, and then there is a set of documents you work with right now. It is probably not very effective to get up and go to the file cabinet every time, so you keep necessary papers on your table. A file cabinet in terms of a computer is your storage device (typically HDD or SSD), and your desk represents the computer's working memory (typically RAM). It's much faster to access RAM, so if certain data is frequently accessed during a particular time period, it's worth keeping it there. That's what we're going to do here.

### Objectives

But before we can start storing necessary data, we need to set up a simple TCP server. You should already be familiar with the [socket module](https://hyperskill.org/learn/step/8670). Create a program that will constantly listen for incoming messages on hostname `0.0.0.0` and port `6379` (which is the default Redis port).

For now, you will have to implement just two commands:

1. `PING` will check that our server works fine and should return PONG as an answer. You can find Redis documentation about this command [here](https://redis.io/docs/latest/commands/ping/).

2. `EXIT`, which does not exist in standard Redis, but we will use it in our implementation to shut down the server from the client side. After receiving this command your future DB should stop working until you rerun it. Probably not the best idea to have it in production but it is perfect for testing purposes.

Note that Redis has a specific format of data sent between the client and the server. You can read about it in details [here](https://redis.io/docs/latest/develop/reference/protocol-spec/#resp-protocol-description). But for this stage, you only need to know:

- Simple string responses always start with `+` followed by the content
- Error messages always start with `-` followed by the content
- Messages always (with minor exceptions) end with `\r\n`

You are expected to both parse the input correctly and return data in a correct format. Refer to the examples below to better understand it.

Note that the Redis protocol also dictates a different format for client messages, but we will deal with it in later stages. For now let's treat both requests and responses as simple strings.

If you are using a UNIX based operating system, make sure to add the following line of code before you bind a port to a server:
```python
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

Adding this line of code will help avoid potential issues with the project tests.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**

Simple PING-PONG communication. Don't forget to exit your event loop if you use one and close the socket after receiving `EXIT`.
```text
> +PING\r\n
+PONG\r\n
> +EXIT\r\n
```

**Example 2**

Since our Tiny Redis only knows 2 commands (for now), any other command should result in an error. Notice that the program should not exit on error; the only way to shut the server down should still be the `EXIT` command.
```text
> +HELLO\r\n
-Unknown command!\r\n
> +EXIT\r\n
```


## Stage 2/6: Argument parsing

### Description

Last time we simplified the Redis protocol a little to not overwhelm ourselves with complex commands and arguments. Now it is time to learn to work with the proper Redis format, after which, we can start using our server with real utilities like `redis-cli` or [redis-py](https://github.com/redis/redis-py) library.

### Objectives

In this stage, you will configure your TCP server to handle real Redis commands with arguments. Also, you will implement the `ECHO` command that simply responds with whatever message the client has sent to your server.

Look at the [Redis serialization protocol specification](https://redis.io/docs/latest/develop/reference/protocol-spec/#arrays) again. It defines the format for client request messages using the following rules:

- Messages start with `*` followed by a number. This tells us the message is an array with that many items. All request messages must be formatted as arrays.
- After the array symbol and number, you add `\r\n` (called CRLF).
- Then you add the actual commands and arguments as "bulk strings." Each bulk string uses this pattern: `$<length>\r\n<data>\r\n` where `<length>` is how many characters are in your string, and `<data>` is your actual command or argument.

So the actual `PING` message we sent in the last stage would look like this: `*1\r\n$4\r\nPING\r\n`.

Based on this information, your goal is to rewrite the parsing rules for client commands (but the response should stay the same). Return an error saying `Parsing error!` for any problem with command formatting.

Additionally, implement command `ECHO`. When the client sends this command, it should be followed by some message. Your server should simply send this message back. Refer to the examples to see the proper formatting.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**

New `ECHO` command should return the exact same message back to the client. Note the length of the string.

Comments above inputs and outputs shows commands stripped from special symbols for convenience.

**Notice** that the string `Hello World!` is just one argument!
```text
# ECHO "You've probably heard me before!"
> *2\r\n$4\r\nECHO\r\n$32\r\nYou've probably heard me before!\r\n
$32\r\nYou've probably heard me before!\r\n
> *1\r\n$4\r\nEXIT\r\n
```

**Example 2**

We won't be testing every possible case, but try to come up with a comprehensive list of things that can go wrong with message formatting from the client side.
```text
> +PING\r\n
-Parsing error!\r\n
> *1\r\n$4\r\nEXIT\r\n
```

> [!NOTE]
> Good news, since we have completely adopted the formatting of the Redis protocol, now you can use redis-cli to interact with your own server. Make sure that your server is running, then open redis-cli in another shell/terminal, and you should be able to talk to your Tiny Redis as if it's a complete grown-up Redis already!


## Stage 3/6: Saving and retrieving data

### Description

The time has come to implement two main features of our in-memory database, without which it wouldn't even be a database at all! Let's configure Tiny Redis to be able to save and retrieve data.

### Objectives

In this stage, you will implement `GET` and `SET` commands on the server. `SET` should save the data sent by the client in memory using a client-specified key, while `GET` will fetch the same data using a provided key.

The implementation details are up to you, but keep in mind the following restrictions:

- The keys must be unique, and if a new value is set with the same key, the previous value should be overwritten.
- If a key does not exist, on `GET` the server should return [null bulk string](https://redis.io/docs/latest/develop/reference/protocol-spec/#null-bulk-strings).
- For the sake of simplicity, we will only use string data types as both keys and values in our testing data.

Commands will be formatted the same way they were formatted in the last stage. Please refer to the examples.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Comments above inputs and outputs shows commands stripped from special symbols for convenience.

**Example 1**

Client can retrieve a value by key they set previously.
```text
# SET champion Carlsen
> *3\r\n$3\r\nSET\r\n$8\r\nchampion\r\n$7\r\nCarlsen\r\n
+OK\r\n
# GET champion
> *2\r\n$3\r\nGET\r\n$8\r\nchampion\r\n
$7\r\nCarlsen\r\n
> *1\r\n$4\r\nEXIT\r\n
```

**Example 2**

Client can't retrieve a value by a key that does not exist.
```text
# GET nepo-titles
> *2\r\n$3\r\nGET\r\n$15\r\nnepo-titles\r\n
$-1\r\n
> *1\r\n$4\r\nEXIT\r\n
```
