from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/" # uniform resource locator

page = requests.get(url) # get request to the website url

# print(page.text)

# make a bs object to scrape, Beautiful Soup parses the page
soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

# find data/text using findall function
# findall can search by tagname, attributes, css class, or string
# by tagname
title = soup.findAll("title")
print(title)

# by attribute
header = soup.findAll(style="text-decoration: none")
print(header)

# by css class
tags = soup.findAll(class_="tags")
print(tags)

# by string
einstein = soup.findAll(string="Albert Einstein")
print(einstein)

# any combination of above
quotes = soup.findAll("span", class_="text")
for quote in quotes:
    print(quote.text)

# find all author
authors = soup.findAll("small", class_="author")
for author in authors:
    print(author.text)

for i in range(len(quotes)):
    print(quotes[i].text)
    print("-", authors[i].text, "\n")
