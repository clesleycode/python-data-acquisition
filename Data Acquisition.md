Data Acquisition with Python & R
==================

Brought to you by [Lesley Cordero](http://www.columbia.edu/~lc2958) and [ADI](https://adicu.com)

## Table of Contents

- [0.0 Setup](#00-setup)
	+ [0.1 Python & Pip](#01-python--pip)
	+ [0.2 R & R Studio](#02-r--r-studio)
	+ [0.3 Other](#03-other)
- [1.0 Background](#10-background)
	+ [1.1 What is Data Science?](#11-what-is-data-science)
		* [1.1.1 What do you mean by data?](#111-what-do-you-mean-by-data)
	+ [1.2 Is data science the same as machine learning?](#12-is-data-science-the-same-as-machine-learning)
	+ [1.3 Why is Data Science important?](#13-why-is-data-science-important)
	+ [1.4 Data Roles](#14-data-roles)
		* [1.4.1 Data Analysis](#141-data-analyst)
		* [1.4.2 Data Engineer](#142-data-engineer)
		* [1.4.3 Data Scientist](#143-data-scientist)
- [2.0 Data Science Process](#20-data-science-process)
	+ [2.1 What is a "Data Science" Problem?](#21-what-is-a-data-science-problem)
	+ [2.2 ...So where do I begin?](#22-so-where-do-i-begin)
	+ [2.3 Given Problem](#23-given-problem)
		* [2.3.1 Open Data](#231-open-data)
	+ [2.4 Given Data](#24-given-data)    
- [3.0 Important Concepts](#30-important-concepts)
	+ [3.1 Machine Learning](#31-machine-learning)
		* [3.1.1 Supervised Learning](#311-supervised-learning)
		* [3.1.2 Unsupervised Learning](#312-unsupervised-learning)
		* [3.1.3 Reinforcement Learning](#313-reinforcement-learning)
- [4.0 Tackling a Data Problem](#40-tackling-a-data-problem)
	+ [4.1 Data Preparation](#41-data-preparation)
	+ [4.2 Data Cleaning](#42-data-cleaning)
	+ [4.3 Data Analysis](#43-data-analysis)
		* [4.4.1 Basics](#431-basics)
		* [4.4.2 Time Series Analysis](#432-time-series-analysis)
		* [4.4.3 Deep Learning](#433-deep-learning)
		* [4.4.4 Natural Language Processing](#434-natural-language-processing)
- [5.0 Resources](#50-resources)


## 0.0 Setup

This guide was written in Python 3.5 and R 3.2.3.

### 0.1 Python & Pip

Download [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/).

### 0.2 R & R Studio

Install [R](https://www.r-project.org/) and [R Studio](https://www.rstudio.com/products/rstudio/download/).

### 0.3 Other

## 1.0 Introduction

The first step of any data science problem is getting your data. As a Data Scientist, you'll spend an incredible amount of time and skills on acquiring, prepping, cleaning, and normalizing your data. In this tutorial, we'll review some of the best tools used in the rhelm of data acquisition. 


## 2.0 Command Line

Through the command line, you can pipe data using sys.stdin and sys.stdout. 

## 2.0 APIs

There are several ways to extract information from the web. Use of APIs is probably the best way to extract data from a website. 

## 4.0 Web Scraping

Web Scraping tools are specifically developed for extracting information from websites. These tools are useful for anyone trying to collect some form of data from the Internet. Web Scraping is the new data entry technique that don’t require repetitive typing or copy-pasting.

Web Scraping mostly focuses on the transformation of unstructured data (HTML format) on the web into structured data (database or spreadsheet)

We'll be analyzing data from the Weather Underground, a website for weather information. APIs are great, but there's still a lot of data locked-up without any APIs, so we'll try a web scraping technique. There also isn't an API always neccessarily available. 

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
1. `<a>`: These always define HTML links, such as with 
``` HTML
<a href="http://byteacademy.co">This is Byte Academy's website!</a>
```
2. `<table>`: HTML tables are defined with this tag, such as:
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
3. `<li>` initializes the beginning of a list. `<ul>` and `<ol>` each define whether it's an unordered list or an ordered list. 


### 4.1 BeautifulSoup

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


## 5.0 Final Words

### 5.1 Resources

