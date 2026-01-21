# Web Scraper

## Project description

You will create a function that takes a website address and a number of webpages as input arguments and then goes all over the website saving every news article on the page to a separate .txt file on your computer.

[View more](https://hyperskill.org/projects/145)


## Stage 1/5: Wanna Talk to the Internet?

### Theory

In the first stage of this project, you need to work with the data extracted from the JSON body response. To notify the server that your program expects the response to be in JSON format, you can pass a header argument with a specified `Accept` field to the `get()` function. The `requests` library has a built-in `json()` decoder. You can use it as follows:
```python
headers = {'Accept': 'application/json'}
response = requests.get(url, headers=headers)
response.json()
```

You can also utilize the `loads()` function from the `json` library. Check out the [json documentation](https://docs.python.org/3/library/json.html#module-json) to learn more about it.

### Description

We use the Internet everyday. Have you ever wondered how your computer communicates with the Global Web? In this stage, we'll learn how to talk to the Internet from your Python script — and interpret the replies! Your program should send an HTTP request to a URL received from the user input. The user input can be a valid resource `https://icanhazdadjoke.com/j/R7UfaahVfFd`. In this case, the program should print out the joke extracted from the `json` body response.

The user may also input an invalid URL or a non-existing resource, for example, `https://icanhazdadjoke.com/j/1`, or a different page (`https://icanhazdadjoke.com/j/authors`). Use `if-else` statements to check the `status_code` or the `json` body response. Print out the `Invalid resource!` error message when the response code is different from 200 or when there is no quote in the `json` body response.

Check the [API docs](https://icanhazdadjoke.com/api) to see the guidelines on how it's used.

### Objectives

In this stage, your program should:

1. Send an HTTP request to a URL received from the user input.
2. Print out the content extracted from the `json` body response.
3. Print out the `Invalid resource!` error message if there's no content or something goes wrong.

### Examples

The greater-than symbol followed by space (`> `) represents the user input. Note that it's not part of the input.

**Example 1**
```text
Input the URL:
> https://icanhazdadjoke.com/j/LBAQ79MJmb

What’s the difference between an African elephant and an Indian elephant? About 5000 miles.
```

**Example 2**
```text
Input the URL:
> https://icanhazdadjoke.com/j/asdfgh

Invalid resource!
```
