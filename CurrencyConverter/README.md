# Currency Converter

## Project description

Want to convert one currency to another? You can go to your bank website and do the math by yourself. Or you can write a program to do it quickly and efficiently! The Currency Converter is a simple console program that calculates the amount of money you get by converting one currency to another.

[View more](https://hyperskill.org/projects/157)


## Stage 1/6: Cryptocurrencies are the new black

### Description

Today we start our new project. It will be a simple currency converter. Every person sometimes needs to convert one currency to another. But we need to start easy, so for now, all you need to do is to print "Meet a conicoin!" Please, make sure that the output formatting of your program follows the example output formatting.

### Objectives

Imagine that there is a cryptocurrency called conicoin ("coni" is just an anagram of the word "coin"). Greet conicoin as shown in the example below.

### Example

Output:
```text
Meet a conicoin!
```


## Stage 2/6: Talking numbers

### Description

Holy moly! Suddenly you remember that back in 2008 you purchased several conicoins! Are you officially rich? Well, we need to find it out. You need to write a program that shows how much you can get after selling your conicoins. One conicoin is 100 dollars. Read your amount of the conicoins as the input, convert them into dollars, and output the result. Also, express your joy, it's important.

### Objectives

Find out if you are rich.

1. Input the amount of your conicoins.
2. Calculate the number of dollars you receive after the conversion. 1 conicoin = 100 dollars, print the result as shown below.
3. Woohoo! You are rich!

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Output:
```text
> 42
I have 42 conicoins.
42 conicoins cost 4200 dollars.
I am rich! Yippee!
```


## Stage 3/6: More interaction

### Description

We are going to make our program more complex. As you remember, the conicoin rate was fixed in the previous stage. But in the real world, things are different. It's time to write a program that takes your conicoins and an up-to-date conicoin exchange rate, then counts how many dollars you would get, and prints the result.

### Objectives

1. Get the number of conicoins from the user input.
2. Get the exchange rate from the user input.
3. Calculate and print the result.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
Please, enter the number of conicoins you have: > 13
Please, enter the exchange rate: > 2
The total amount of dollars: 26
```

**Example 2:**
```text
Please, enter the number of conicoins you have: > 128
Please, enter the exchange rate: > 3.21
The total amount of dollars: 410.88
```


## Stage 4/6: Going global

### Description

You can convert your conicoins into dollars, cool. What if you want a different currency? What if you're going to Morocco tomorrow? You'll need some dirhams, that's for sure. We need to improve our converter.

Take the imaginary exchange rates below and modify your program to work with 5 different currencies:

- RUB – Russian Ruble; 1 conicoin = 2.98 RUB;
- ARS – Argentine Peso; 1 conicoin = 0.82 ARS;
- HNL – Honduran Lempira; 1 conicoin = 0.17 HNL;
- AUD – Australian Dollar; 1 conicoin = 1.9622 AUD;
- MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.

Take the number of conicoins as the user input, сonvert it to the specified currencies, and round the result to two decimals using the Python built-in function. Notice that the input number can have a fractional part!

### Objectives

1. Get the number of conicoins from user input.
2. Print how much you will get in all five currencies mentioned above.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1:**
```text
> 17
I will get 50.66 RUB from the sale of 17.0 conicoins.
I will get 13.94 ARS from the sale of 17.0 conicoins.
I will get 2.89 HNL from the sale of 17.0 conicoins.
I will get 33.36 AUD from the sale of 17.0 conicoins.
I will get 3.54 MAD from the sale of 17.0 conicoins.
```

**Example 2:**
```text
> 3.5
I will get 10.43 RUB from the sale of 3.5 conicoins.
I will get 2.87 ARS from the sale of 3.5 conicoins.
I will get 0.6 HNL from the sale of 3.5 conicoins.
I will get 6.87 AUD from the sale of 3.5 conicoins.
I will get 0.73 MAD from the sale of 3.5 conicoins.
```


## Stage 5/6: JSON and the Rates

### Description

In the previous stages, we worked with different real-world currencies but the exchange rates were fixed. Unfortunately (or not, depending on your political stance), we don't really have fixed exchange rates in today's world. At this stage, you will have to work with the Internet to get the information! The [FloatRates](http://www.floatrates.com/json-feeds.html) site contains a special JSON page for each currency. Your task is to make requests to these pages and download the actual data on the exchange rates of the US dollar and the euro. Remember, that the data is stored in JSON format.

### Objectives

There are many currency codes, for example, RUB, ARS, ILS, AUD, MAD, etc. Your task is to return the information about the exchange rates from the site specified above for a given currency and USD and EUR.

1. Take the currency code as the user input.
2. Make a request to `http://www.floatrates.com/daily/YOUR_CURRENCY_CODE.json`. Don't forget to replace `YOUR_CURRENCY_CODE` in the link with your currency and put the code in lowercase.
3. Print your result for USD and EUR.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

> [!NOTE]
> Be aware that the dictionary elements are unordered. The results of your output may differ, as the service updates the data once in twelve hours. Don't hesitate to print the whole string for your own interest, but it is not a part of the stage.

The output for AUD:
```text
> AUD
{'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 0.65826859178751, 'date': 'Mon, 12 Aug 2024 09:55:14 GMT', 'inverseRate': 1.5191367360921}
{'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 0.60285890590547, 'date': 'Mon, 12 Aug 2024 09:55:14 GMT', 'inverseRate': 1.65876292148}
```
