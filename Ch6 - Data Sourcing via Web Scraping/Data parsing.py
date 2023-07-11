from bs4 import BeautifulSoup
import urllib
import urllib.request
import re

with urllib.request.urlopen(
        'https://raw.githubusercontent.com/BigDataGal/Data-Mania-Demos/master/IoT-2018.html') as response:
    html = response.read()

soup = BeautifulSoup(html, 'lxml')
print(type(soup))

# parsing data
print(soup.prettify()[0:100])

# Getting data from a parse tree
text_only = soup.get_text()
print(text_only)
print('---------------------------------------------------------------------')

# Searching and retrieving data from a parse tree
print(soup.find_all('li'))
print('---------------------------------------------------------------------')

# Retrieving tags by filtering with keyword args
print(soup.find_all(id='link 7'))
print('---------------------------------------------------------------------')

# Retrieving tags by filtering with string args
print(soup.find_all('ol'))
print('---------------------------------------------------------------------')

# Retrieving tags by filtering with list objects
print(soup.find_all(['ol', 'b']))
print('---------------------------------------------------------------------')

# Retrieving tags by filtering with regex
t = re.compile('t')
for tag in soup.find_all(t):
    print(tag.name)
print('---------------------------------------------------------------------')

# Retrieving tags by filtering with boolean value
for tag in soup.find_all(True):
    print(tag.name)
print('---------------------------------------------------------------------')

# Retrieving weblinks by filtering with string objects
for link in soup.find_all('a'):
    print(link.get('href'))
print('---------------------------------------------------------------------')


# Retrieving strings by filtering with regex
print(soup.find_all(string=re.compile('data')))
