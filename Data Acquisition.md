Data Acquisition with Python & R
==================

Brought to you by [Lesley Cordero](http://www.columbia.edu/~lc2958) and [ADI](https://adicu.com)

## Table of Contents

- [0.0 Setup](#00-setup)
	+ [0.1 Python & Pip](#01-python--pip)
	+ [0.2 R & R Studio](#02-r--r-studio)
	+ [0.3 Virtual Environment](#03-virtual-environment)
- [1.0 Introduction](#10-introduction)
- [2.0 Reading, Writing, and Handling Data Files](#20-reading-writing-and-handling-files)
	+ [2.1 CSV files](#21-csv-files)
		* [2.1.1 CSV](#211-csv)
		* [2.1.2 Pandas](#212-pandas)
	+ [2.2 JSON](#22-json)
- [3.0 APIs](#30-apis)
	+ [3.1 GET request](#31-get-request)
	+ [3.2 Status Codes](#32-status-codes)
- [4.0 Web Scraping](#40-web-scraping)
	+ [4.1 HTML](#41-html)
	+ [4.2 BeautifulSoup](#42-beautiful-soup)
- [5.0 Resources](#50-resources)


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
pip3 install BeautifulSoup
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
install.packages("") 
install.packages("")
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

To execute the visualizations in matplotlib, do the following:

```
cd ~/.matplotlib
nano matplotlibrc
```
And then, write `backend: TkAgg` in the file. Now you should be set up with your virtual environment!

Cool, now we're ready to start! 

## 1.0 Introduction

All data problems begin with a question and end with a narrative construct that provides a clear answer. From there, the next step is getting your data. As a Data Scientist, you'll spend an incredible amount of time and skills on acquiring, prepping, cleaning, and normalizing your data. In this tutorial, we'll review some of the best tools used in the rhelm of data acquisition. 

But first, let's go into the differences between Data Acquisition, Preparation, and Cleaning. 

### 1.1 Data Acquisition

Data Acquisition is the process of getting your data, hence the term <i>acquisition</i>. Data doesn't come out of nowhere, so the very first step of any data science problem is going to be getting the data in the first place. 

### 1.2 Data Preparation

Once you have the data, it might not be in the best format to work with. You might have scraped a bunch of data from a website, but need it is the form of a dataframe to work with it in an easier manner. This process is called data preparation - preparing your data in a format that's easiest to form with.

### 1.3 Data Cleaning

Once your data is being stored or handled in a proper manner, that might still not be enough. You might have missing values or values that need normalizing. These inconsistencies that you fix before analysis refers to data cleaning. 

## 2.0 Reading, Writing, and Handling Data Files

The simplest way of acquiring data is downloading a file - either from a website, straight from your desktop, or elsewhere. Once the data is downloaded, you'll open the files for reading and possible writing. 

### 2.1 CSV files

Very often, you'll have to work with CSV files. A csv file is a comma-separated values file stores tabular data in plain text. 

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
Not too horrible

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


## 5.0 Final Words

### 5.1 Resources

