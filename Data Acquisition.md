Data Acquisition with Python & R
==================

Brought to you by [Lesley Cordero](http://www.columbia.edu/~lc2958), [Byte Academy](byteacademy.co) and [ADI](https://adicu.com)

## Table of Contents

- [0.0 Setup](#00-setup)
	+ [0.1 Python & Pip](#01-python--pip)
	+ [0.2 R & R Studio](#02-r--r-studio)
	+ [0.3 Virtual Environment](#03-virtual-environment)
- [1.0 Introduction](#10-introduction)
	+ [1.1 Data Acquisition](#11-data-acquisition)
	+ [1.2 Data Preparation](#12-data-preparation)
	+ [1.3 Data Cleaning](#13-data-cleaning)
- [2.0 Reading, Writing, and Handling Data Files](#20-reading-writing-and-handling-files)
	+ [2.1 CSV files](#21-csv-files)
		* [2.1.1 CSV](#211-csv)
		* [2.1.2 Pandas](#212-pandas)
		* [2.1.3 R Programming](#213-r-programming)
	+ [2.2 JSON](#22-json)
		* [2.2.1 jsonlite](#221-jsonlite)
- [3.0 APIs](#30-apis)
	+ [3.1 GET request](#31-get-request)
	+ [3.2 Status Codes](#32-status-codes)
	+ [3.3 APIs with R](#33-apis-with-r)
- [4.0 Web Scraping](#40-web-scraping)
	+ [4.1 HTML](#41-html)
	+ [4.2 BeautifulSoup](#42-beautiful-soup)
	+ [4.3 rvest](#43-rvest)
- [5.0 Advanced Web Scraping](#50-advanced-web-scraping)
	+ [5.1 Sitemaps](#51-sitemaps)
	+ [5.2 Estimating Website Size](#52-estimating-website-size)
	+ [5.3 Regular Expressions](#53-regular-expressions)
		* [5.3.1 Simplest Form](#531-simplest-form)
		* [5.3.2 Case Sensitivity](#532-case-sensitivity)
		* [5.3.3 Disjunctions](#533-disjunctions)
		* [5.3.4 Ranges](#534-ranges)
		* [5.3.5 Exclusions](#535-exclusions)
		* [5.3.6 Question Marks](#536-question-marks)
		* [5.3.7 Kleene Star](#537-kleene-star)
		* [5.3.8 Wildcards](#538-wildcards)
		* [5.3.9 Kleene+](#539-kleene-+)
	+ [5.4 REs & BeautifulSoup](#54-res--beautifulsoup)
	+ [5.5 Lambda Expressions](#55-lambda-expressions)
- [6.0 Crawling with Scrapy](#60-crawling-with-scrapy)
	+ [6.1 Scrapy](#61-scrapy)
	+ [6.2 Extract the Data](#62-extract-the-data)
	+ [6.3 Expanding](#63-expanding)	
	+ [6.4 Multiple Pages](#64-multiple-pages)
- [7.0 Final Words](#70-final-words)
	+ [7.2 Mini Courses](#72-mini-courses)

## 0.0 Setup

This guide was written in Python 3.5 and R 3.2.3.

### 0.1 Python & Pip

Download [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/).

Then, on your command line, install the needed modules as follows:

``` 
pip3 install csv
pip3 install pandas
pip3 install json
pip3 install requests
pip3 install BeautifulSoup4
pip3 install scrapy
```

### 0.2 R & R Studio

Install [R](https://www.r-project.org/) and [R Studio](https://www.rstudio.com/products/rstudio/download/).

Next, to install the R packages, cd into your workspace, and enter the following, very simple, command into your bash: 

```
R
```

This will prompt a session in R! From here, you can install any needed packages. For the sake of this tutorial, enter the following into your terminal R session:

```
install.packages("jsonlite")
install.packages("httr") 
install.packages("rvest")
```

### 0.3 Virtual Environment

If you'd like to work in a virtual environment, you can set it up as follows: 
```
pip3 install virtualenv
virtualenv your_env
```
And then launch it with: 
```
source your_env/bin/activate
```

Now you should be set up with your virtual environment!

Cool, now we're ready to start! 

## 1.0 Introduction

All data problems begin with a question and end with a narrative construct that provides a clear answer. From there, the next step is getting your data. As a Data Scientist, you'll spend an incredible amount of time and skills on acquiring, prepping, cleaning, and normalizing your data. In this tutorial, we'll review some of the best tools used in the rhelm of data acquisition. 

But first, let's go into the differences between Data Acquisition, Preparation, and Cleaning. 

### 1.1 Data Acquisition

Data Acquisition is the process of getting your data, hence the term <i>acquisition</i>. Data doesn't come out of nowhere, so the very first step of any data science problem is going to be getting the data in the first place. 

### 1.2 Data Preparation

Once you have the data, it might not be in the best format to work with. You might have scraped a bunch of data from a website, but need it in the form of a dataframe to work with it in an easier manner. This process is called data preparation - preparing your data in a format that's easiest to form with.

### 1.3 Data Cleaning

Once your data is being stored or handled in a proper manner, that might still not be enough. You might have missing values or values that need normalizing. These inconsistencies that you fix before analysis refers to data cleaning. 

## 2.0 Reading, Writing, and Handling Data Files

The simplest way of acquiring data is downloading a file - either from a website, straight from your desktop, or elsewhere. Once the data is downloaded, you'll open the files for reading and possible writing. 

### 2.1 CSV files

Very often, you'll have to work with CSV files. A csv file is a comma-separated values file stores tabular data in plain text. 

In the following examples, we'll be working with NBA data, which you can download from [here](https://github.com/ByteAcademyCo/data-acq/blob/master/nba.csv).

#### 2.1.1 CSV 

Python has a csv module, which you can utilize to work with CSV files.

``` python
import csv
```

Then, with the following 4 lines, you can print each row
``` python
with open('nba.csv', ‘rt') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)
```
Fairly straightforward, but let's see how else we can accomplish this. 

#### 2.1.2 Pandas

Alternatively, you can use Pandas. Pandas is great for working with CSV files because it handles DataFrames. 

We begin by importing the needed libraries: pandas.

``` python
import pandas as pd
```

Then we use pandas to read the CSV file and show the first few rows. 
``` python
task_data = pd.read_csv("nba.csv")
task_data.head()
```
As you can see, by using pandas, we're able to fasten the process of viewing our data, as well as view it in a much more readable format. 

#### 2.1.3 R Programming

We've just gone through how to read CSV files in Python. But how do you do this in R? Pretty simply, actually. R has built in functions to handle CSV files, so you don't even have to use a library to accomplish what we just did with Python.

``` R
data <- read.csv("nba.csv")
```

### 2.2 JSON

Because HTTP is a protocol for transferring text, the data you request through a web API (which we'll go through soon enough) needs to be serialized into a string format, usually in JavaScript Object Notation (JSON). JavaScript objects look quite similar to Python dicts, which makes their string representations easy to interpret:

```
{ 
 "name" : "Lesley Cordero",
 "job" : "Data Scientist",
 "topics" : [ "data", "science", "data science"] 
}
```

Python has a module sepcifically for working with JSON, called `json`, which we can use as follows:

``` python
import json
serialized = """ { 
 "name" : "Lesley Cordero",
 "job" : "Data Scientist",
 "topics" : [ "data", "science", "data science"] 
} """
```
Next, we parse the JSON to create a Python dict, using the json module: 
 
``` python
deserialized = json.loads(serialized)
print(deserialized)
```

And we get this output:

```
{'name': 'Lesley Cordero', 'job': 'Data Scientist', 'topics': ['data', 'science', 'data science']}
```

#### 2.2.1 jsonlite

Now, in R, working with JSON can be a bit more complicated. Unlike Python, R doesn't have a data type that resembles JSON closely (dictionaries in Python). So we have to work with what we do have, which is lists, vectors, and matrices.

Working with the same data from the Python example, we have:

``` python
serialized = '{ 
 "name" : "Lesley Cordero",
 "job" : "Data Scientist",
 "topics" : [ "data", "science", "data science"] 
} '
```

Now, if we want to properly load this into R, we'll be using the `jsonlite` library. 

``` R
library("jsonlite")
```
Once we've loaded the library, we'll use the `fromJSON` function to convert this into a data type R is more familiar with: <b>lists</b>.

``` R
l <- fromJSON(serialized, simplifyVector=TRUE)
```

Notice that `simplifyVector` is set to `TRUE`. When simplifyMatrix is enabled, JSON arrays containing equal-length sub-arrays simplify into a matrix. 

And to convert this back to JSON, we type:

``` R
toJSON(l, pretty=TRUE)
```
Not too horrible!

## 3.0 APIs

There are several ways to extract information from the web. Use of APIs, Application Program Interfaces, is probably the best way to extract data from a website. APIs are especially great if your data is constantly changing. Many websites have public APIs providing data feeds via JSON or some other format. 

There are a number of ways to access these APIs from Python. In order to get the data, we make a request to a webserver, hence an easy way is to use the `requests` package. 

### 3.1 GET request

There are many different types of requests. The most simplest is a GET request. GET requests are used to retrieve your data. In Python, you can make a get request to get the latest position of the international space station from the `OpenNotify` API.

``` python
import requests
response = requests.get("http://api.open-notify.org/iss-now.json")
```

If you print `response.status_code`, you'll get 

``` 
200
```

Which brings us to status codes. 

### 3.2 Status Codes

What we just printed was a status code of `200`. Status codes are returned with every request made to a web server and indicate what happened with a request. The following are the most common types of status codes:

- `200` - everything worked as planned!
- `301` - the server is redirecting you to anotehr endpoint (domain).
- `400` - it means you made a bad request by not sending the right data or some other error.
- `401` - you're not authenticated, which means you don't have access to the server.
- `403` - this means access is forbidden. 
- `404` - whatever you tried to access wasn't found. 

Notice that if we try to access something that doesn't exist, we'll get a `404` error:

``` python
response = requests.get("http://api.open-notify.org/iss-pass")
print(response.status_code)
```

Let's try a get request where the status code returned is `404`. 
``` python
response = requests.get("http://api.open-notify.org/iss-pass.json")
print(response.status_code)
```
Like we mentioned before, this indicated a bad request. This is because it requires two parameters, as you can see [here](http://open-notify.org/Open-Notify-API/ISS-Pass-Times/). 

We set these with an optional `params` variable. You can opt to make a dictionary and then pass it into the `requests.get` function, like follows:

``` python 
parameters = {"lat": 40.71, "lon": -74}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
```

You can skip the variable portion with the following instead: 
``` python
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
```

If you print the content of both of these with `response.content`, you'll get: 
```
b'{\n  "message": "success", \n  "request": {\n    "altitude": 100, \n    "datetime": 1441417753, \n    "latitude": 40.71, \n    "longitude": -74.0, \n    "passes": 5\n  }, \n  "response": [\n    {\n      "duration": 329, \n      "risetime": 1441445639\n    }, \n    {\n      "duration": 629, \n      "risetime": 1441451226\n    }, \n    {\n      "duration": 606, \n      "risetime": 1441457027\n    }, \n    {\n      "duration": 542, \n      "risetime": 1441462894\n    }, \n    {\n      "duration": 565, \n      "risetime": 1441468731\n    }\n  ]\n}'
```
This is pretty messy, but luckily, we can clean this up into JSON with:

``` python
data = response.json()
```

And we get: 
``` 
{'response': [{'risetime': 1441456672, 'duration': 369}, {'risetime': 1441462284, 'duration': 626}, {'risetime': 1441468104, 'duration': 581}, {'risetime': 1441474000, 'duration': 482}, {'risetime': 1441479853, 'duration': 509}], 'message': 'success', 'request': {'latitude': 37.78, 'passes': 5, 'longitude': -122.41, 'altitude': 100, 'datetime': 1441417753}}
```

### 3.3 APIs with R

So far we've seen APIs with Python. Let's take a look on how you can use R to do some simple API calls. We'll be working with the `httr` library and the EPDB API, which we load in the next three lines:

``` R
library("httr")
url  <- "http://api.epdb.eu"
path <- "eurlex/directory_code"
```

With `httr`, you can make GET requests, like this:
``` R
raw.result <- GET(url=url, path=path)
```
If you check out what `raw.result` is, you'll see the following information:
```
Response [http://api.epdb.eu/eurlex/directory_code/]
  Date: 2017-02-06 21:41
  Status: 200
  Content-Type: application/json
  Size: 121 kB
```

Now let's pull the name entities from this GET request:
``` R
names(raw.result)
```

Which results in, as we'd expect:
```
 [1] "url"         "status_code" "headers"     "all_headers" "cookies"    
 [6] "content"     "date"        "times"       "request"     "handle" 
```

You can extract each of the entitites above with the `$` character, like this:
``` R
raw.result$status_code
```

which results in a `200` status code!

## 4.0 Web Scraping

Web Scraping tools are specifically developed for extracting information from websites. Web Scraping mostly focuses on the transformation of unstructured data (HTML format) on the web into structured data (database or spreadsheet).

### 4.1 HTML

While performing web scraping, we deal with html tags. Thus, we must have good understanding of them. Below is the basic syntax of HTML:

``` html
<!DOCTYPE html> 
<html>
	<body>
		<h1> First Heading </h1>
		<p> First Paragraph </p>
	</body>
</html>
```
Let's break down each of these tags:

1. `<!DOCTYPE html>`: This is the initial HTML declaration.
2. `<html>`: The HTML document is going to be contained within this tag.
3. `<body>`: This is where the visible portion of the HTML document is between. 
4. `<h1>`: This is an HTML heading.
5. `<p>`: HTML paragraphs are defined here. 

We've also got the following tags:
- `<a>`: These always define HTML links, such as with 
``` HTML
<a href="http://byteacademy.co">This is Byte Academy's website!</a>
```
- `<table>`: HTML tables are defined with this tag, such as:
*Note that the `<tr>`are rows and `<td>` defines columns. 
``` HTML
<table style="width:100%">
	<tr>
		<td>Lesley</td>
		<td>Cordero</td>
		<td>24</td>
	</tr>
	<tr>
		<td>Helen</td>
		<td>Chen</td>
		<td>22</td>
	</tr>
</table>
```
This will yield the following:
```
Lesley		Cordero		24
Helen		Chen		22
```
- `<li>` initializes the beginning of a list. `<ul>` and `<ol>` each define whether it's an unordered list or an ordered list. 


### 4.2 BeautifulSoup

BeautifulSoup is used to parse the data.

``` python
import requests
from bs4 import BeautifulSoup
```

``` python
wiki = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
page = requests.get(wiki)
html = page.content
```

``` python
soup = BeautifulSoup(html)
```

Now, let's explore this webpage! 

``` python
soup.title
```
This outputs the title of the wikipedia page: 
```
<title>List of states and territories of the United States - Wikipedia</title>
```

The string version of this can be obtained with:

``` python
soup.title.string
```
With `soup.a`, we can output the links under the `<a>` tag. We get the following:
```
<a id="top"></a>
```

But this only allows us to have one output. If we want to extract all the links within `<a>`, we will use `find_all()`, as the following:
``` python
all_links = soup.find_all("a")
for i in all_links:
	print(i.get("href"))
```

Since we're looking for the capital of each state, let's use `find_all` to retrieve the table tags:
``` python
all_tables = soup.find_all('table')
```

Now we have to identify the right table. We filter this by figuring out what the attribute class name is. In chrome, you can check the class name by right click on the table of web page. Then you click "Inspect" and copy the class name. You also go through the output of above command find the class name of right table.

``` python
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
```

We're now going to store the data from the website. We'll grab the first few columns, so we'll initialize a list for each of these here:

``` python
A = []
B = []
C = []
```
Next, is to actually grab the needed data and add it to each list. We iterate through the scraped data, row by row:

``` python
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') 
    if len(cells) == 9 or len(cells) == 8: 
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
```

Here, we actually create the DataFrame with pandas: 

``` python
import pandas as pd
df=pd.DataFrame(A, columns=['Number'])
df['State/UT'] = B
df['Admin_Capital'] = C
```

### 4.3 rvest

Now we'll try scraping a website with R. R has a library called `rvest` which allows you scrape the HTML from any webpage. In the following two lines, we call this library and take the HTML with the `read_html` function. 

``` R
library(rvest)
movie <- read_html("http://www.imdb.com/title/tt1490017/")
```

Let's now scape some information from the website. `html_nodes` easily extract pieces out of HTML documents using css selectors while `html_text` extracts attributes, text, and tag name from the HTML. Using these two functions, we can extract the rating for this movie. 
``` R
rating <- movie %>%
	html_nodes("strong span") %>%
	html_text() %>%
	as.numeric() 
```
And we get:
```
[1] 7.8
```

Next, let's get the cast of the movie:
``` R
cast <- movie %>%
	html_nodes("#titleCast .itemprop span") %>%
	html_text()
```
Which pulls out:
```
 [1] "Will Arnett"     "Elizabeth Banks" "Craig Berry"     "Alison Brie"    
 [5] "David Burrows"   "Anthony Daniels" "Charlie Day"     "Amanda Farinos" 
 [9] "Keith Ferguson"  "Will Ferrell"    "Will Forte"      "Dave Franco"    
[13] "Morgan Freeman"  "Todd Hansen"     "Jonah Hill"     
```

And lastly, we extract the first movie review on the site:
``` R
review <- movie %>%
	html_nodes("#titleUserReviewsTeaser p") %>%
	html_text()
```

And here it is!
``` 
[1] "I was the only adult who didn't bring kids to the theater and all I can say is that I was leading the clapping when the credits rolled.\"The Lego Movie\" was an awesome, super creative, and extremely satisfying film for all ages- that is, if you have ever played with Legos. Even people that have never bought a Lego set will this enjoy this awesomely humorous and in the end, heartfelt movie.(Notice I am using the word awesome a lot, because one cannot stop singing the \"Everything is awesome\" song played in the movie. Too catchy!)The creators did a wonderful job putting all the classic things about Legos and making a new movie packed with humor.The voice actors were outstanding. You can tell they really enjoyed doing the movie and put in a lot of effort. Liam Neeson was fantastic as the Good Cop/Bad Cop. But the most credit to the success of this movie goes to Will Farrell who played the villain, President Business. He gives such a great effort in this movie which allows you to laugh, smile, and want more Lego awesomeness.I give the Lego movie a big two thumbs up and is by far the best picture I've seen in a few months. Highly recommend this movie to all Lego lovers who have a passion to build and create something awesome, just like the movie makers created this amazingly, AWESOME, film."
```

## 5.0 Advanced Web Scraping


### 5.1 Sitemaps

The Sitemaps protocol allows a webmaster to inform search engines about URLs on a website that are available for crawling. A Sitemap is an XML file that lists the URLs for a site. It allows webmasters to include additional information about each URL: when it was last updated, how often it changes, and how important it is in relation to other URLs in the site. This allows search engines to crawl the site more intelligently. Sitemaps are a URL inclusion protocol and complement robots.txt, a URL exclusion protocol.

An example of what a sample XML sitemap might look like is:

``` 
<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

   <url>

      <loc>http://www.example.com/</loc>

      <lastmod>2005-01-01</lastmod>

      <changefreq>monthly</changefreq>

      <priority>0.8</priority>

   </url>

</urlset> 
```

### 5.2 Estimating Website Size

The size of the website will affect how you crawl it. If the website is just a few hundred URLs, such as our example website, efficiency is not important. However, if the website has over a million web pages, downloading each sequentially would take months. 


### 5.3 Regular Expressions

A regular expression is a sequence of characters that define a string.

#### 5.3.1 Simplest Form

The simplest form of a regular expression is a sequence of characters contained within <b>two backslashes</b>. For example, <i>python</i> would be  

``` 
\python
```

#### 5.3.2 Case Sensitivity

Regular Expressions are <b>case sensitive</b>, which means 

``` 
\p and \P
```
are distinguishable from eachother. This means <i>python</i> and <i>Python</i> would have to be represented differently, as follows: 

``` 
\python and \Python
```

We can check these are different by running:

``` python
import re
re1 = re.compile('python')
print(bool(re1.match('Python')))
```

#### 5.3.3 Disjunctions

If you want a regular expression to represent both <i>python</i> and <i>Python</i>, however, you can use <b>brackets</b> or the <b>pipe</b> symbol as the disjunction of the two forms. For example, 
``` 
[Pp]ython or \Python|python
```
could represent either <i>python</i> or <i>Python</i>. Likewise, 

``` 
[0123456789]
```
would represent a single integer digit. The pipe symbols are typically used for interchangable strings, such as in the following example:

```
\dog|cat
```

#### 5.3.4 Ranges

If we want a regular expression to express the disjunction of a range of characters, we can use a <b>dash</b>. For example, instead of the previous example, we can write 

``` 
[0-9]
```
Similarly, we can represent all characters of the alphabet with 

``` 
[a-z]
```

#### 5.3.5 Exclusions

Brackets can also be used to represent what an expression <b>cannot</b> be if you combine it with the <b>caret</b> sign. For example, the expression 

``` 
[^p]
```
represents any character, special characters included, but p.

#### 5.3.6 Question Marks 

Question marks can be used to represent the expressions containing zero or one instances of the previous character. For example, 

``` 
<i>\colou?r
```
represents either <i>color</i> or <i>colour</i>. Question marks are often used in cases of plurality. For example, 

``` 
<i>\computers?
```
can be either <i>computers</i> or <i>computer</i>. If you want to extend this to more than one character, you can put the simple sequence within parenthesis, like this:

```
\Feb(ruary)?
```
This would evaluate to either <i>February</i> or <i>Feb</i>.

#### 5.3.7 Kleene Star

To represent the expressions containing zero or <b>more</b> instances of the previous character, we use an <b>asterisk</b> as the kleene star. To represent the set of strings containing <i>a, ab, abb, abbb, ...</i>, the following regular expression would be used:  
```
\ab*
```

#### 5.3.8 Wildcards

Wildcards are used to represent the possibility of any character and symbolized with a <b>period</b>. For example, 

```
\beg.n
```
From this regular expression, the strings <i>begun, begin, began,</i> etc., can be generated. 

#### 5.3.9 Kleene+

To represent the expressions containing at <b>least</b> one or more instances of the previous character, we use a <b>plus</b> sign. To represent the set of strings containing <i>ab, abb, abbb, ...</i>, the following regular expression would be used:  

```
\ab+
```

### 5.4 REs & BeautifulSoup 

If the previous section on regular expressions seemed a little disjointed, here’s where it all ties together. BeautifulSoup and regular expressions go hand in hand when it comes to scraping the Web. In fact, most functions that take in a string argument will also take in a regular expression as well. 

Looking at [this](http://www.pythonscraping.com/pages/page3.html) webpage, we'll see that there are product images of the following form:

``` HTML
<img src="../img/gifts/img3.jpg">
```
If we wanted to grab URLs to all of the product images, it might seem fairly straightforward: just grab all the image tags using `.findAll("img")`. Unfortunately, there’s a problem. There are “extra” images (i.e, logos), often have hidden images, and blank images used for spacing and aligning elements, and other random image tags you might not be aware of.

The solution is to look for another approach. In this case, we can look at the file path of the product images. You've seen this part before:

``` python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
```

This prints out only the relative image paths that start with ../img/gifts/img and end in `.jpg`:

``` python
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
	print(image["src"])
```

A regular expression can be inserted as any argument in a BeautifulSoup expression, allowing you a great deal of flexibility in finding target elements.

### 5.5 Lambda Expressions

Recall, a lambda expression is a function that is passed into another function as a variable. Instead of defining a function as f(x, y), you may define a function as f(g(x), y), or even f(g(x), h(x)).

BeautifulSoup allows us to pass certain types of functions as parameters into the findAll function. The only restriction is that these functions must take a tag object as an argument and return a boolean. Every tag object that BeautifulSoup encounters is evaluated in this function, and tags that evaluate to “true” are returned while the rest are discarded.

For example, the following retrieves all tags that have exactly two attributes:

``` python
soup.findAll(lambda tag: len(tag.attrs) == 2)
```
which will find tags like following:

``` HTML
<div class="body" id="content"></div>
<span style="color:red" class="title"></span>
```

Using lambda functions in BeautifulSoup, selectors can act as a great substitute for writing a regular expression, if you’re comfortable with writing a little code.


## 6.0 Crawling with Scrapy

One of the challenges of writing web crawlers is that you’re often performing the same tasks again and again: find all links on a page, evaluate the difference between internal and external links, go to new pages. Scrapy is a Python library that handles much of the complexity of finding and evaluating links on a website, crawling domains or lists of domains with ease. 

To begin this tutorial with Scrapy, first let's create a directory to work with. In your terminal,

``` bash
mkdir brickset-scraper
```

Then enter that directory:

``` bash
cd brickset-scraper
```

We'll be working with classes here, so instead of entering the code into your Python environment, let's work in a file called `scraper.py`.

``` bash
vim scraper.py
```

Great, now we're set to start.

### 6.1 Scrapy

We'll start by making a very basic scraper that uses Scrapy as its foundation. To do that, we'll create a Python class that subclasses scrapy.Spider, a basic spider class provided by Scrapy. This class will have two required attributes:

- `name` - just a name for the spider.
- `start_urls` - a list of URLs that you start to crawl from

First, we import scrapy so that we can use the classes that the package provides. Next, we take the Spider class provided by Scrapy and make a subclass out of it called BrickSetSpider. 

Recall, that the Spider subclass will have methods and behaviors that define how to follow URLs and extract data from the pages it finds, but it doesn't know where to look or what data to look for. By subclassing it, we can give it that information. Finally, we give the spider the name brickset_spider and give our scraper a single URL to start from:

``` python
import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']
```

Now let's test out the scraper. Scrapy comes with its own command line interface to streamline the process of starting a scraper, so start your scraper with the following command:

``` bash
scrapy runspider scraper.py
```

This gets you the following output:

``` bash
2016-09-22 23:37:45 [scrapy] INFO: Scrapy 1.1.2 started (bot: scrapybot)
2016-09-22 23:37:45 [scrapy] INFO: Overridden settings: {}
2016-09-22 23:37:45 [scrapy] INFO: Enabled extensions:
['scrapy.extensions.logstats.LogStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.corestats.CoreStats']
2016-09-22 23:37:45 [scrapy] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 ...
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2016-09-22 23:37:45 [scrapy] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 ...
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2016-09-22 23:37:45 [scrapy] INFO: Enabled item pipelines:
[]
2016-09-22 23:37:45 [scrapy] INFO: Spider opened
2016-09-22 23:37:45 [scrapy] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2016-09-22 23:37:45 [scrapy] DEBUG: Telnet console listening on 127.0.0.1:6023
2016-09-22 23:37:47 [scrapy] DEBUG: Crawled (200) <GET http://brickset.com/sets/year-2016> (referer: None)
2016-09-22 23:37:47 [scrapy] INFO: Closing spider (finished)
2016-09-22 23:37:47 [scrapy] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 224,
 'downloader/request_count': 1,
 ...
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2016, 9, 23, 6, 37, 45, 995167)}
2016-09-22 23:37:47 [scrapy] INFO: Spider closed (finished)
```

First, the scraper initialized and loaded additional components and extensions it needed to handle reading data from URLs.

Next, it used the URL we provided in the `start_urls` list and grabbed the HTML.

And lastly, it passed that HTML to the parse method, which doesn't do anything since we haven't written it yet. This causes it to just end without doing anything.


### 6.2 Extract the Data

So far we've pulled down the pages, but we haven't actually scraped anything yet. If you look at the webpage we're scraping, you'll notice the following structure:

- The header is present in every page.
- There's search data.
- Then there's data that's actually formed in the form of a list or table. 


When writing a scraper, it's a good idea to look at the source of the HTML file and familiarize yourself with the structure. So here it is, with some things removed for readability:

``` HTML
<body>
  <section class="setlist">
    <article class='set'>
      <a class="highslide plain mainimg" href=
      "http://images.brickset.com/sets/images/10251-1.jpg?201510121127"
      onclick="return hs.expand(this)"><img src=
      "http://images.brickset.com/sets/small/10251-1.jpg?201510121127"
      title="10251-1: Brick Bank"></a>
      <div class="highslide-caption">
        <h1><a href='/sets/10251-1/Brick-Bank'>Brick Bank</a></h1>
        <div class='tags floatleft'>
          <a href='/sets/10251-1/Brick-Bank'>10251-1</a> <a href=
          '/sets/theme-Advanced-Models'>Advanced Models</a> <a class=
          'subtheme' href=
          '/sets/theme-Advanced-Models/subtheme-Modular-Buildings'>Modular
          Buildings</a> <a class='year' href=
          '/sets/theme-Advanced-Models/year-2016'>2016</a>
        </div>
        <div class='floatright'>
          &copy;2016 LEGO Group
        </div>
        <div class="pn">
          <a href="#" onclick="return hs.previous(this)" title=
          "Previous (left arrow key)">&#171; Previous</a> <a href="#"
          onclick="return hs.next(this)" title=
          "Next (right arrow key)">Next &#187;</a>
        </div>
      </div>
      ...
    </article>
    <article class='set'>

      ...

    </article>
</section>
</body>
```

We'll proceed at follows:

1. First, we'll grab each set by looking for the parts of the page that have the data we want.
2. Fo each of these sets, we'll grab the data we want from it by pulling the data out of the HTML tags.

`scrapy` grabs data based on the selectors that you provide. Recall, selectors are patterns we can use to find one or more elements on a page so we can then work with the data within the element. 

We’ll use CSS selectors since CSS is the easier option and a perfect fit for finding all the sets on the page. If you look at the HTML for the page, you'll see that each set is specified with the class set. Since we're looking for a class, we'd use `.set` for our CSS selector. All we have to do is pass that selector into the response object, like this:

``` python
    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            pass
```

This code grabs all the sets on the page and loops over them to extract the data. Now let’s extract the data from those sets so we can display it.

If we look into the HTML again, we'll see that the name of each set is stored within an `a` tag and inside an `h1` tag:

``` python
<h1><a href='/sets/10251-1/Brick-Bank'>Brick Bank</a></h1>
```

The brickset object we’re looping over has its own css method, so we can pass in a selector to locate child elements. Modify your code as follows to locate the name of the set and display it:

``` python
    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 a ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
            }
```

We appended `::text` to our selector for the name, which is a CSS pseudo-selector that fetches the text inside of the a tag. We also called `extract_first()` on the object returned by brickset.`css(NAME_SELECTOR)` because we just want the first element that matches the selector. This gives us a string, rather than a list of elements.

Let's run the script again. This time we'll get:

``` bash
...
[scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'name': 'Brick Bank'}
[scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'name': 'Volkswagen Beetle'}
[scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'name': 'Big Ben'}
[scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'name': 'Winter Holiday Train'}
...
```

Now we've got the names of the sets!


### 6.3 Expanding

We want to add new selectors so we can get images and other data, so let's take another look at the HTML for a specific set:

``` HTML
<article class="set">
  <a class="highslide plain mainimg" href="http://images.brickset.com/sets/images/10251-1.jpg?201510121127" onclick="return hs.expand(this)">
    <img src="http://images.brickset.com/sets/small/10251-1.jpg?201510121127" title="10251-1: Brick Bank"></a>
  ...
  <div class="meta">
    <h1><a href="/sets/10251-1/Brick-Bank"><span>10251:</span> Brick Bank</a> </h1>
    ...
    <div class="col">
      <dl>
        <dt>Pieces</dt>
        <dd><a class="plain" href="/inventories/10251-1">2380</a></dd>
        <dt>Minifigs</dt>
        <dd><a class="plain" href="/minifigs/inset-10251-1">5</a></dd>
        ...
      </dl>
    </div>
    ...
  </div>
</article>
```

Notice the image is stored in the `src` attrice of an `img` tag, which is inside of an `a` tag.

``` python
    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 a ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }
```

To get the number of pieces, we have to use XPath because it's too complex to be represented with CSS selectors. 

Once again, let's run the script and we get: 

``` bash
2016-09-22 23:52:37 [scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'minifigs': '5', 'pieces': '2380', 'name': 'Brick Bank', 'image': 'http://images.brickset.com/sets/small/10251-1.jpg?201510121127'}
2016-09-22 23:52:37 [scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'minifigs': None, 'pieces': '1167', 'name': 'Volkswagen Beetle', 'image': 'http://images.brickset.com/sets/small/10252-1.jpg?201606140214'}
2016-09-22 23:52:37 [scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'minifigs': None, 'pieces': '4163', 'name': 'Big Ben', 'image': 'http://images.brickset.com/sets/small/10253-1.jpg?201605190256'}
2016-09-22 23:52:37 [scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'minifigs': None, 'pieces': None, 'name': 'Winter Holiday Train', 'image': 'http://images.brickset.com/sets/small/10254-1.jpg?201608110306'}
2016-09-22 23:52:37 [scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'minifigs': None, 'pieces': None, 'name': 'XL Creative Brick Box', 'image': '/assets/images/misc/blankbox.gif'}
2016-09-22 23:52:37 [scrapy] DEBUG: Scraped from <200 http://brickset.com/sets/year-2016>
{'minifigs': None, 'pieces': '583', 'name': 'Creative Building Set', 'image': 'http://images.brickset.com/sets/small/10702-1.jpg?201511230710'}
```

Notice the new information presented! 

### 6.4 Multiple Pages

We’ve extracted data from that initial page, but we're not looking at the rest of the results. The whole point of a spider is to detect and traverse links to other pages and grab data from those pages too.

You might have noticed the buttons that proceed to the next page. We'll check out the HTML for this button:

``` HTML
<ul class="pagelength">

  ...

  <li class="next">
    <a href="http://brickset.com/sets/year-2017/page-2">&#8250;</a>
  </li>
  <li class="last">
    <a href="http://brickset.com/sets/year-2016/page-32">&#187;</a>
  </li>
</ul>
```

There's a li tag with the class of `next`, and inside that tag, there's an a tag with a link to the next page. All we have to do is tell the scraper to follow that link if it exists.

``` python
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback = self.parse
            )
```            
First, we defined a selector for the "next page" link, extract the first match, and check if it exists. `callback = self.parse` passes back the HTML for the next page.

This is the key piece of web scraping: finding and following links. In this example, it’s very linear; one page has a link to the next page until we’ve hit the last page, But you could follow links to tags, or other search results, or any other URL you'd like.

Now, let's run it again! Notice it goes on into 23 pages and 779 sets!


## 7.0 Final Words

And that's a wrap for the Data Acquisition portion of this course. Next, we'll head into the Data Preparation portion of this course, where we'll overview data formatting, pandas, dpylr, and more. 

### 7.2 Mini Courses

Learn about courses [here](www.byteacademy.co/all-courses/data-science-mini-courses/).

[Python 101: Data Science Prep](https://www.eventbrite.com/e/python-101-data-science-prep-tickets-30980459388) <br>
[Intro to Data Science & Stats with R](https://www.eventbrite.com/e/data-sci-109-intro-to-data-science-statistics-using-r-tickets-30908877284) <br>
[Data Acquisition Using Python & R](https://www.eventbrite.com/e/data-sci-203-data-acquisition-using-python-r-tickets-30980705123) <br>
[Data Visualization with Python](https://www.eventbrite.com/e/data-sci-201-data-visualization-with-python-tickets-30980827489) <br>
[Fundamentals of Machine Learning and Regression Analysis](https://www.eventbrite.com/e/data-sci-209-fundamentals-of-machine-learning-and-regression-analysis-tickets-30980917759) <br>
[Natural Language Processing with Data Science](https://www.eventbrite.com/e/data-sci-210-natural-language-processing-with-data-science-tickets-30981006023) <br>
[Machine Learning with Data Science](https://www.eventbrite.com/e/data-sci-309-machine-learning-with-data-science-tickets-30981154467) <br>
[Databases & Big Data](https://www.eventbrite.com/e/data-sci-303-databases-big-data-tickets-30981182551) <br>
[Deep Learning with Data Science](https://www.eventbrite.com/e/data-sci-403-deep-learning-with-data-science-tickets-30981221668) <br>
[Data Sci 500: Projects](https://www.eventbrite.com/e/data-sci-500-projects-tickets-30981330995)

