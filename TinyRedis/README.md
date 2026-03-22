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
