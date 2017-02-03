Data Acquisition with Python & R
==================

Brought to you by [Lesley Cordero](http://www.columbia.edu/~lc2958) and [ADI](https://adicu.com)

## Table of Contents

- [0.0 Setup](#00-setup)
	+ [0.1 Python & Pip](#01-python--pip)
	+ [0.2 R & R Studio](#02-r--r-studio)
	+ [0.3 Virtual Environment](#03-virtual-environment)
- [1.0 Introduction](#10-introduction)
- [2.0 Reading and Writing Files](#20-reading-and-writing-files)
	+ [2.1 CSV files](#21-csv-files)
- [3.0 APIs](#30-apis)
- [4.0 Web Scraping](#40-web-scraping)
	+ [4.1 HTML](#41-html)
	+ [4.2 BeautifulSoup](#42-beautiful-soup)
- [5.0 Resources](#50-resources)


## 0.0 Setup

This guide was written in Python 3.5 and R 3.2.3.

### 0.1 Python & Pip

Download [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/).

### 0.2 R & R Studio

Install [R](https://www.r-project.org/) and [R Studio](https://www.rstudio.com/products/rstudio/download/).

### 0.3 Other

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

All data problems begin with a question and end with a narrative construct that provides
a clear answer. From there, the next step is getting your data. As a Data Scientist, you'll spend an incredible amount of time and skills on acquiring, prepping, cleaning, and normalizing your data. In this tutorial, we'll review some of the best tools used in the rhelm of data acquisition. 


## 2.0 Reading and Writing Files

The simplest way of acquiring data is downloading a file - either from a website, straight from your desktop, or elsewhere. Once the data is downloaded, you'll open the files for reading and possible writing. 


### 2.1 CSV files

Very often, you'll have to work with CSV files. A csv file is a comma-separated values file stores tabular data in plain text. 

``` python
from urllib.request import urlretrieve
import pandas as pd
```

``` python
url = "https://gist.githubusercontent.com/jhamrick/cfa18fcd3032ba435ec78a194b1447be/raw/4a4052c56161df8e454a61ab5286a769799c64b8/task_data.csv"
urlretrieve(url, "task_data.csv")
```

``` python
task_data = pd.read_csv("task_data.csv")
task_data.head()
```

## 3.0 APIs

There are several ways to extract information from the web. Use of APIs is probably the best way to extract data from a website. Many websites have public APIs providing data feeds via JSON or some other format. There are a number of ways to access these APIs from Python. One easy way is to use the `requests` package. 

``` python
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
A=[]
B=[]
C=[]
```

``` python
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') 
    print(row)
    if len(cells) == 9 or len(cells) == 8: 
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
```

``` python
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
```


## JSONS

Because HTTP is a protocol for transferring text, the data you request through a web API needs to be serialized into a string format, usually in JavaScript Object Notation (JSON). JavaScript objects look quite similar to Python dicts, which makes their string representations easy to interpret:

```
{ 
 "name" : "Lesley Cordero",
 "job" : "Data Scientist",
 "topics" : [ "data", "science", "data science"] 
}
```

Python has a built in `json` module, which we can use as follows:

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

## 5.0 Final Words

### 5.1 Resources

