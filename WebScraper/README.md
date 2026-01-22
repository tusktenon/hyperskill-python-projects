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


## Stage 2/5: The Beautiful Soup Ingredients

### Theory

Some Internet pages might get automatically translated according to your computer's settings. Although this might be useful in everyday life, in this project we ask you to output the data in English. To force `requests` library to return a page in English, you can use `headers` with `Accept-Language` parameter set to the value `en-US,en;q=0.5`:
```python
response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
```

Note that the structure of the page might be different in cases when you use this header and when you don't (even if your default language is English).

However, not all servers or web applications respect the `Accept-Language` header. Some websites might ignore the header entirely and serve content in the default language set by the server or based on other criteria like IP geolocation.

`q`: This is a quality factor, which is a decimal value between 0 and 1 that indicates the client's preference for each language. The higher the `q` value, the higher the preference. For example, `en-US,en;q=0.5` means the client prefers U.S. English, but will accept any English content if U.S. English is unavailable, with a lower preference.

### Description

We know how to send HTTP requests and get responses. In the previous stage, the example URL responded with the `json` body, this is how the `REST` resources communicate with a client. We, humans, go to websites to access the Internet. We also have browsers, but sometimes we need to parse the website's content automatically. Parsing is one of the ways to scrape a webpage.

Parsing website data begins with the inspection of the page source code with browser built-in tools. Usually, the desired information can be distinguished by some unique attributes or a set of attributes, for example, a css class name. We need to determine these attributes and then make our parsing tool (in our case, the `beautifulsoup` library) do the magic for us.

### Objectives

1. Take a link to the [nature.com](https://www.nature.com/) article as input. This is an example of a correct link: [https://www.nature.com/articles/d41586-023-00103-3](https://www.nature.com/articles/d41586-023-00103-3). The link to an article always contains the word "articles" in it.
2. Download the webpage content, parse it using the `beautifulsoup` library.
3. Print out the article's heading and short summary as a dictionary. You can find the heading in the `<title>` tag. The summary can be found in the `<meta>` tag with the `{'name': 'description'}` attribute.

If the link doesn't have an article or is not a nature.com resource, the program should respond with an error message `Invalid page!`.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input. Each example corresponds to a separate execution.

**Example 1**
```text
Input the URL:
> https://www.nature.com/articles/d41586-023-00103-3

{"title": "Green electronics rely on materials that grow on trees", "description": "Compounds derived from eucalyptus and other plants are formulated into an ink for printing electronic components."}
```

**Example 2**
```text
Input the URL:
> https://www.imdb.com/name/nm0001191/

Invalid page!
```

**Example 3**
```text
Input the URL:
> https://www.google.com/

Invalid page!
```


## Stage 3/5: What the File?

### Theory

Apart from writing files in the usual text mode, it is also possible to write files in binary mode. It means that Python won't encode the data while writing it to the file. This can be done by passing the argument `'wb'` to the `open()` function instead of the usual `'w'`:
```python
file = open('file.html', 'wb')
```

To retrieve a page's content while using the `requests` library, the `content` attribute can be used:
```python
page_content = requests.get(input_url).content
```

Binary mode (`'wb'`) is necessary when writing HTML content to a file. This prevents Python from trying to interpret the content as text, which could corrupt binary data like images, videos, or special characters embedded in the HTML.

### Description

In previous stages, we retrieved the results and printed them out on the screen. It's handy for one-time running programs or for debugging, but if we want to reuse the data (and that's the case most of the time), storing it is more effective. The simplest way to store data is to write it to a file on your computer.

In this stage, we are going to store the state of a webpage at the moment when the program is executed. It means that we need to get its source code, the content, and save it to an `.html` file.

### Objectives

1. Create a program that retrieves the page's source code from a user input URL. Please, don't decode the page's content.
2. Save the page's content to the `source.html` file. Please, write the file in binary mode.
3. Print the `Content saved.` message if everything is OK (Don't forget to add a check for the `status_code`).
4. If something is wrong, print the message `The URL returned X`, where `X` is the received error code.

### Examples

The program receives a URL to retrieve the data from the user input, saves the data to the `source.html` file, and responds with the successful completion message. Otherwise, it should notify a user about an error.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input. Each example corresponds to a separate execution.

**Note:** Instead of using magic numbers like 200 or 404 while comparing with `status_code`, you can import `HTTPStatus` from `http` module.

**Example 1**
```text
Input the URL:
> https://www.facebook.com/

Content saved.
```

**Example 2**
```text
Input the URL:
> http://google.com/asdfg

The URL returned 404!
```
