# Web

Work with XML, XPahts, HTTP requests, servers

`2020/03/17, Jaroslav Langer`

## MENU

+ [XML](#xml)
+ [HTTP](#http)
+ [Scrapping](#scrapping)
+ [Servers](#Servers)


## XML

## eTree XML

### Modules

```py
import xml.etree.ElementTree as et
# Or, dunno the diference
from lxml import etree
```

### Parse xml

```py
# Parse from file #
tree = et.parse('country_data.xml')
# Parse from string #
tree = et.fromstring(response.text)

# Parsing with specified parser #
# Create parser #
parser = et.XMLParser(encoding="utf-8")

# Parse with parser #
tree = et.parse('country_data.xml', parser=parser)
et.fromstring(response.text, parser=parser)
```

### Atributes of elements

```py
# Get root element #
root = tree.getroot()
el.tag
el.attrib
el.text
```

### childs are iterable

```py
el[3]

for child in el:
    print(child.tag, child.attrib)
```

### find element

```py
rank = country.find('rank').text

# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")
# Find only first element with correct xpath
# result = xroot.find("/html")
# print(result.decode('utf-8'))
```

### xpath

**tag**

Selects all child elements with the given tag. For example, spam selects all child elements named spam, and spam/egg selects all grandchildren named egg in all children named spam. {namespace}* selects all tags in the given namespace, {*}spam selects tags named spam in any (or no) namespace, and {}* only selects tags that are not in a namespace.

Changed in version 3.8: Support for star-wildcards was added.

**\***

Selects all child elements, including comments and processing instructions. For example, */egg selects all grandchildren named egg.

**.**

Selects the current node. This is mostly useful at the beginning of the path, to indicate that it’s a relative path.

**//**

Selects all subelements, on all levels beneath the current element. For example, .//egg selects all egg elements in the entire tree.

**..**

Selects the parent element. Returns None if the path attempts to reach the ancestors of the start element (the element find was called on).

**[\@attrib]**

Selects all elements that have the given attribute.

**[@attrib='value']**

Selects all elements for which the given attribute has the given value. The value cannot contain quotes.

**[tag]**

Selects all elements that have a child named tag. Only immediate children are supported.

**[.='text']**

Selects all elements whose complete text content, including descendants, equals the given text.

New in version 3.7.

**[tag='text']**

Selects all elements that have a child named tag whose complete text content, including descendants, equals the given text.

**[position]**

Selects all elements that are located at the given position. The position can be either an integer (1 is the first position), the expression last() (for the last position), or a position relative to the last position (e.g. last()-1).

[Top](#Web) |
[source](https://docs.python.org/3/library/xml.etree.elementtree.html) |
[source2](http://vyuka.ookami.cz/materialy/python/xml/etree.xml)


## Beautiful soup

```py
from bs4 import BeautifulSoup

# Parse with BEAUTIFULSOUP #
# Get soup object #
soup = BeautifulSoup(response.text)

# Access html soup objects #
soup.body.div.find(id="bodyWrapper").div.div.div.div.div.div.div
```

---

## HTTP

+ [Requests](#requests)

## Requests

```py
import requests
```

### Get request

```py
response = requests.get(url)

# File downloads on click, download with request #
response = requests.get(download_url)

# Get html from url #
response = requests.get(url)
html = response.text
```

### Response

```py
# Response text and status code#
response.text
response.status_code
```
[Source](https://requests.readthedocs.io/en/master/user/quickstart/)

[Top](#Web)

---

## Scrapping

### Download full website

```py
from pywebcopy import save_webpage
# Write directly with pywebcopy #
kwargs = {'bypass_robots': True, 'project_name': project_name}
save_webpage(url, download_folder, **kwargs)
```

[Top](#Web)

---

## Server

[Top](#Web)

---
