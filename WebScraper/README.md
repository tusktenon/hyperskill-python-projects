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


## Stage 4/5: The Soup is Real

### Description

We now have a good deal of knowledge and experience, so let's put it all together and create your first real web scraper. Most of the time, the reason why people create parse-and-scrape programs is to automate the routine tasks of retrieving large data from a website. For example, every machine learning task requires some **training data**. Let's imagine you're doing research based on the recent science news. For that research, you'll need to have the most recent articles with the type "News" that are posted on the Nature journal website. Each article should be saved to a separate `.txt` file named after the article's title.

### Objectives

1. Create a program that takes the `https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3` URL and then goes over the page source code searching for articles.

2. Detect the article type and the link to view the article tags and their attributes.

3. Save the contents of each article of the type "News", that is, the text from the article body without the tags, to a separate file named `%article_title%.txt`. When you save the file, replace the whitespaces in the name of the article with underscores and remove punctuation marks in the filename. Use `string.punctuation` to remove punctuation. Strip all trailing whitespaces in the article body and title. For example, the article with the title "*Legendary Arecibo telescope will close forever — scientists are reeling*" should be saved to the file named *Legendary_Arecibo_telescope_will_close_forever_scientists_are_reeling.txt*.

4. (Optional) You may output some result message once the saving is done, but it is not required.

We need to inspect each article to find the tags that represent the article's contents.

Here's a breakdown of what you need to do with the source HTML:

1. **Find Articles:** Each article on the webpage is enclosed within `<article>` tags. So, to locate articles, look for these tags. The `<article>` tag is a semantic HTML5 element used to represent an independent piece of content, such as a blog post, news article, or forum post. In the context of web scraping, it serves as a container for each article on the webpage. By targeting `<article>` tags, we're specifically focusing on the main content sections of the webpage where articles are displayed.

2. **Identify Article Type:** Within each `<article>`, the type of the article is specified inside a `<span>` tag. This `<span>` tag has a `data-test` attribute with the value representing the article type (`article.type`). The `<span>` tag is a generic inline container typically used for styling purposes or to group inline elements. In this case, it's used to enclose metadata about the article type. The `data-test` attribute serves as a marker or identifier added by the website's developers to facilitate automated testing or data extraction. By using this attribute, we can reliably locate and extract the article type information associated with each `<span>` tag.

3. **Access Article Contents Link:** Each article has a link to its contents, which is inside an `<a>` tag. This `<a>` tag has a `data-track-action` attribute with the value "view article". The `<a>` tag is used to create hyperlinks, allowing users to navigate to different pages or sections of a website. Here, it's employed to create links to view the full contents of each article. The `data-track-action` attribute is a custom attribute added by the website to track user interactions, specifically actions related to viewing articles. By targeting `<a>` tags with this attribute, we can identify and extract the links leading to the complete article content.

4. **Retrieve Article Body:** After clicking on the link to view an article, the body of the article is displayed. This content is wrapped inside a `<p>` tag with the attribute `{"class": "article__teaser"}`. Save this content of the article. The `<p>` tag is used to define paragraphs of text within HTML documents. In this scenario, it's utilized to encapsulate the main body of each article. The `class` attribute is a standard HTML attribute used to assign one or more classes to an element, enabling CSS styling and JavaScript manipulation. By targeting `<p>` tags with the specified class (`"article__teaser"`), we can pinpoint the paragraphs containing the summary of each article, which is typically displayed on the article listing page.

> [!NOTE]
> Keep in mind that while the above methods work for scraping this specific website, they might not work for another one. The way we scrape depends on how each website is built. Different websites use different tags, attributes, and even dynamic content loading methods.

Make sure your output file is binary with the UTF-8 character encoding.

### Example

This time, the program should not take the URL from the input: hard-code it inside the program. Below is an example of the output:
```text
Saved articles:  ['COVID_research_updates_Immune_responses_to_coronavirus_persist_beyond_6_months.txt', 'What_scientists_really_think_about_the_ethics_of_facial_recognition_research.txt', 'Legendary_Arecibo_telescope_will_close_forever_scientists_are_reeling.txt', 'What_the_data_say_about_asymptomatic_COVID_infections.txt']
```

The main goal is to save the articles with the correct article bodies once the program has been executed.


## Stage 5/5: Soup, Sweet Soup

### Description

You've done an amazing job in the previous stage! Remember we mentioned retrieving large data? Let's improve your program by making it parse multiple website pages. To make it even more useful, let's also implement the opportunity to parse several kinds of articles at once.

### Objectives

1. Improve your code so that the function can take two parameters from the user input: the number of pages (an integer) and the type of articles (a string). The integer with the number of pages specifies the number of pages on which the program should look for the articles.
2. Go back to the `https://www.nature.com/nature/articles?sort=PubDate&year=2020` website and find out how to navigate between the pages with the requests module changing the URL.
3. Create a directory named `Page_N` (where `N` is the page number corresponding to the number input by the user) for each page. Search and collect all articles page by page; filter all the articles by the article type and put all the articles that are found on the page with the matched type to the directory `Page_N`. Mind that when the user enters some number, for example, 4, the program should search all pages up to that number and the respective folders (Folder 1, Folder 2, Folder 3, Folder 4) should be created.
4. Save the articles to separate `*.txt` files. Keep the same processing of the titles for the filenames as in the previous stage. You can give users some feedback on completion, but it is not required.

If there's no articles on the page, your program should still create a folder, but in this case the folder would be empty.

### Example

The program takes two input values from the user and then continues to process the Nature website data.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```text
> 4
> Nature Briefing
Saved all articles.
```

The main goal is to save the articles with the correct article bodies once the program has been executed.

**Hint:** There is no need to extract the articles with the type that varies from the user's input type.
