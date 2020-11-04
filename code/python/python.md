# Python

`2020/10/24, Jaroslav Langer`

## Content <!-- omit in toc -->
- [Tutorials](#tutorials)
- [How to start](#how-to-start)
  - [Installation](#installation)
  - [Run python](#run-python)
- [Basics](#basics)
  - [First things first](#first-things-first)
  - [Comments](#comments)
  - [Printing](#printing)
  - [Variables](#variables)
  - [Handy methods](#handy-methods)
  - [Data types](#data-types)
  - [String](#string)
  - [Bytes](#bytes)
  - [Conditions](#conditions)
  - [Loops](#loops)
  - [Collections](#collections)
  - [Methods for loops](#methods-for-loops)
  - [Math](#math)
  - [Random](#random)
  - [Imports](#imports)
  - [Inputs, outputs](#inputs-outputs)
  - [Files](#files)
  - [os](#os)
  - [Asserting](#asserting)
  - [Json](#json)
  - [Exceptions](#exceptions)
- [Advanced](#advanced)
  - [Regex](#regex)
  - [Lambda](#lambda)
  - [Datetime](#datetime)
  - [argparse](#argparse)
  - [Compress, decompress, checksum](#compress-decompress-checksum)
  - [underscored names in python](#underscored-names-in-python)
  - [ctypes](#ctypes)
  - [Python 2 differences](#python-2-differences)


## Tutorials

[Tutorial place](https://realpython.com/)

## How to start

### Installation

#### Venv

```sh
# activate enviroment
source .env_name/source/activate
# deactivate
deactivate
```

#### pip

```sh
# Insall package
pip3 install package_name
# Show package info
pip3 show package_name
# Update package
pip3 install --upgrade package_name
```

### Run python

#### Terminal

#### Scripts

Python is and excelent language for writing scripts. Every script on linux should start with. Otherwise, there will be misunderstanding between python2 and 3 guys.
```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
For usage python files as scripts is highly recommend to use following
```py
if __name__ == "__main__":
    #This code will be executed only, if the file was called as a script, not imported
```

## Basics

### First things first

Everything in a python is an **object**. String is an object, list is an object. 
So almost anything has some methods already prepare for you. 
With `dir` function you can see all the atributes and methods of the object.

```py 
dir(anything)
```

### Comments

```py
# Oneline coment

"""
multiline comment
"""

'''
multiline comment
'''
```

#### Docstrings

Every file, class, function can have doc string (__doc__).
Write docstrings, they are beatiful.

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: my beautiful code name
Author: my beautiful name, email
Description:
blaaaaaaaaaa
"""

def fu():
    """function docstring"""

class cla:
    """class docstring"""
```

### Printing

Do not use variable printing for code debugging, use debugger instead!
(However to use printing for local simple testing is absolutely great thing.)

```py
variable = "var"
var2 = "2"
var3 = 3

print(variable)
print("---")

# No newline at the end
print(variable, end="")
print("---")

# More variables
print(variable, var2, var3)
print("---")

# Different separator
print(variable, var2, var3, sep=", ")
print("---")

# Personal recomendation for var printing (bit advanced, but good practise)
four = 2*2
my_array = [7,"6","five",four,[0,1,2]]
print('"len(my_array[2])": {}'.format(len(my_array[2])))
```

Output

```out
var
---
var---
var 2 3
---
var, 2, 3
---
"len(my_array[2])": 4
```

### Variables

```py
# Float NaN
NaN = float("NaN")
```

### Handy methods

#### len()
priceless method, can be used for number of characters of a string as well as number of elements of an array

#### Slices

Basicly anything, which can be iterated retrieve slice, after useing [:]
```py
string[firstLetter:LetterNotToBeSeen]
array[firstItem:] #To the end
array[firstItem:-1] #To the end
array[firstItem:-5] #To the fifth last
```

Examples
```py
# Slice DOCTYPE out of html #
text = text[len('<!DOCTYPE html>\n'):]
```

### Data types

#### type and isinstance

Recognize type of a passed object
```py
var = {1: "2"}

# Check if types are equal
type(var) == type({}) # True

# However based on the PEP recommendation, types should never be compared like that, instead use
isinstance(a, dict) # True
```

### String

There is four types how to quote a string
```py
# Two equivalens how write single-line string
'string'
"another string"
# Two equivalens how write multi-line string
'''
multiline string
'''
"""
another multiline string
"""
```
Raw string
```py
r'in this string, the \n won\'nt be and newline'
```

#### Format and f string

```py
# Using stirng.format()
pathToNewFile = '{folder}{file}.{fileType}'.format(
    folder=download_folder, file=xlsName, fileType='xls')

# Curly braces to remain
string = "{{double clurly braces will be formated as one".format()
# escaping does not work
string = "\{ this will raise an ValueError".format()

# f string
pathToNewFile = f'{download_folder}{xlsName}.{"xls"}'

# Format float precision
a = 1/3
print("{:.2f}".format(a)) # 0.33
```

#### String functions

```py
# lower
"sTrInG StRiNg".lower() # "string"
# upper
"sTrInG StRiNg".upper() # "STRING STRING"
# capitalize
"sTrInG StRiNg".capitalize() # "String string"

# slit
"string string2".split()
# join
' '.join(['string', 'string2', 'string3'])
# strip
"          string                ".strip()

# find
"string about nothing".find('abo')
# rfind
".hiden_file_.txt".rfind('.')

# count
question = "Hi mom, how much coins i need to buy coin keeper for my coin sessions?"
question.count("coin") # 3

# isnumeric - check if every character is unicode numeric
"1234".isnumeric() # True
"1234.2".isnumeric() # False
```

[is numeric (tutorials point)](https://www.tutorialspoint.com/python/string_isnumeric.htm)

### Bytes

```py
bytes_1 = b"Bytes form this string"
bytes_2 = "Bytes form this string".encode()

string_from_bytes = bytes_1.decode()
```

[link](https://www.tutorialspoint.com/python/string_decode.htm)

### Conditions

ternary assigning
```
variable = value if (condition) else otherValue
```

### Loops

[top](#python)
```py
for x in almostAnything:
    print(x)
```

### Collections

#### Lists

```py
l = ["a", "b"]
ll = ["c", "d"]
# Append
l.append(ll)
# Pop
l.pop()
# Extend
ll.extend(l)
# Insert
ll.insert(index, item)
# Convert string to list
list("All the beautiful strings")

# Sort
l.sort()
# Ascending/descending, preprocess keys by a function (-> sort names from longest)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

def cmp_len(x):
    return len(x)

cars.sort(reverse=True, key=cmp_len)

# Or with lambda (bit advanced)
cars.sort(reverse=True, key=lambda x: len(x))
```

[sort example](https://www.w3schools.com/python/ref_list_sort.asp)

##### Copy vs. deep copy

```py
# Shallow copy, changes in list2 affects list1
list2 = list1
# Two independent lists, changes in one doesn't effect the other one
list2 = list1.copy()
```

#### Dictionary

```py
my_dict = {"Key": "value", "k": 1, "list": [1,2,3]}
dict_tmp = dict([("another", "key"), ("and_many", "more")])
# Add key-value pair
my_dict["new_key"] = "anything"
# Add all key-values from another dictionary
my_dict.update(dict_tmp)
```

```py
# For loop with dictionaries
for key in myDict:
    print(myDict[key])

for key, value in myDict.items():
    print(key)
    print(value)
```

#### Comprehensions

```py
crazy_big = 34526
crazy_fifth = round(crazy_num/5)

# list comprehension
my_list = [x for x in range(crazy_fifth, crazy_big, crazy_fifth)]

# dict comprehension
my_dict = {str(item): item%2354 for item in my_list}

# set comprehension
my_set = {val for val in my_dict.values()}
```

[set comprehension](https://python-reference.readthedocs.io/en/latest/docs/comprehensions/set_comprehension.html)

### Methods for loops

```py
# zip
ids = ["34925705", "09548622", "24641309"]
names = ["John","Peter", "Anthony"]
nicnames = ["Joeeyyy", "Pete", "Toeney"]

transformed = [[id, na, ni] for id, na, ni in zip(ids, names, nicnames)]
[['34925705', 'John', 'Joeeyyy'], ['09548622', 'Peter', 'Pete'], ['24641309', 'Anthony', 'Toeney']]

# enumerate
galleries_without_number = ["Great Gallery", "Magnificent Gallery", "The Gallery"]
id_galery_dict = {-n: v for n,v in enumerate(galleries_without_number, start=1)}
```

### Math

```py
# Round(float, precision)
round(1.242345, 3)

# Multiple comparisons one line
20 > 13 > 10 # True
(20 > 13) > 10 # False
```

[Round function (w3school)](https://www.w3schools.com/python/ref_func_round.asp)
[Multiple comparism (python 2.3 doc, still valid)](https://docs.python.org/2.3/ref/comparisons.html)

### Random

```py
# Random float from range (0,10)
f = uniform(0, 10)

# Random integer from range
i = randrange(0, 101, 1)

# Random item of list
NAMES = ["Alice", "Bob", "Chuck"]
item = choice(NAMES)
```

[Random library (python documentation)](https://docs.python.org/3/library/random.html)

### Imports
```py
from xy import xyz as x
```

### Inputs, outputs

#### Input arguments

```py
import sys
```
first argument is name of a script with the path you run it
```
print ("the script has the name: {}".format(sys.argv[0]))
```
number of arguments
```
print ("Number of arguments: {}".format(len(sys.argv[0])))
```

#### Standard input

```py
import sys

for line in sys.stdin: # From standard input
    print(line) # to standard output
```

### Files

```py
with open(PATH_TO_FILE, mode='r') as f:
    line = f.readline()
```
multiple files
```py
with open("file_1.txt", mode="r") as f_in, open("file_2.txt", mode="w") as f_out:
    f_out.write(f_in.readline())
```

[source](https://www.w3schools.com/python/python_file_write.asp)

#### Modes

- x: create file, error if already exists
- r: 
- rb: 
- r+: 
- w: rewrite existing, create if does not exist
- wb: 
- w+: 
- wb+:
- a: append to existing, create if does not exist
- ab: 
- a+: 
- ab+:

[source](https://stackabuse.com/file-handling-in-python/)

#### Text files

```py
# Write xls from response.text to file #
pathToNewFile = '{folder}{file}'.format(folder=download_folder, file=xlsName)
# print('pathToNewFile', pathToNewFile)
with open(pathToNewFile, mode='tx') as newFile:
    newFile.write(response.text)
```

#### Binary files

```py
with open('obrazek.png', mode='rb') as f:
    data = f.read(NUMBER_OF_BYTES)
    f.tell()                # tells position
    #Doesn't move the reading head
    #return at least desired number of bytes
    f.peek(NUMBER_OF_BYTES) 
```

[source](http://vyuka.ookami.cz/materialy/python/files/basics.xml)

### os

```py
import os

# Get full (absolute) path (maybe antipattern, dunno)
os.path.abspath("./build/knapsack.so")
```

### Asserting
```py
assert(len(tables)==1), f"len(tables) = {len(tables)}"
```

### Json

```py
import json

json_string = json.dumps({1: "yes", 2: "no", 3: "maybe"})
```

### Exceptions

```py
import json

json_string = "my json string"

# This is dangerous, if the string is not loadable, it will raise error
json_dict = json.loads(json_string)
```

Way to handle these is by try-except structures

```py
import json

json_string = "my json string"

try:
    json_dict = json.loads(json_string)
except json.decoder.JSONDecodeError as e:
    print(f'It was not posible to load "json_string" as a dictionary.',
        f'Error: "{e}", json_string: "{json_string}".')
```

## Advanced

### Regex

```py
import re

# Using more flags
x = re.findall(r'CAT.+?END','Cat \n eND',flags=re.I | re.DOTALL)
```

#### Match 

Matches from the begining of the string

#### fullmatch

the whole pattern must match

[Module re](https://docs.python.org/2/library/re.html)
[Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

#### The special characters

| Pattern | Match group |
| --- | --- |
| `.` | in the default mode, this matches any character except a newline |
| `*` | Causes the resulting RE to match 0 or more repetitions of the preceding character |
| `+` | Causes the resulting RE to match 1 or more repetitions of the preceding character or RE |
| `?` | Causes the resulting RE to match 0 or 1 repetitions of the preceding RE |
| `|` | `A|B`, where A and B can be arbitrary REs, creates a regular expression that will match either A or B|
| `[]` | matches set of character (examples: [ce] match {'c', 'e'}, [c-e], match {'c', 'd', 'e'} [ce+] match {'c', 'd', '+'}, [^c] match anything except 'c')
| `\A` | matches only at the start of the string |
| `\Z` | matches only at the end of the string |
| `\d` | Matches any Unicode decimal digit |
| `\D` | matches any non-digit character; this is equivalent to the class [^0-9] |
| `\s` | Matches Unicode whitespace characters |
| `\S` | Matches any character which is not a whitespace character |
| `\w` | Matches Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore |
| `\W` | Matches any character which is not a word character. This is the opposite of \w |
| `(?=...)` | Matches if ... matches next, but doesn’t consume any of the string |
| `(?!...)` | Matches if ... doesn’t match next |
| `(?<=...)` | Matches if the current position in the string is preceded by a match for ... that ends at the current position |
| `(?<!...)` | Matches if the current position in the string is not preceded by a match for .... |

### Lambda

```py
candidates[DEGREE] = candidates[[DEGREE, DEGREE_TMP]].apply(lambda x:
    np.nan if (pd.isnull(x[0]) & pd.isnull(x[1])) else
        x[0] if pd.isnull(x[1]) else
            x[1] if pd.isnull(x[0]) else x[0]+x[1], axis=1)
```

[More information](https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/)

### Datetime


```py
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
```

[datetime link](https://www.programiz.com/python-programming/datetime/current-time)

```
from datetime import datetime

datetime_str = '09/19/18 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)  # printed in default format
```

[work with datetime](https://www.journaldev.com/23365/python-string-to-datetime-strptime) string to datetime

### argparse

```py
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t", "--type", choices=[NA, AA], help="reformat nucleic acid or amino acid sequence")
    args = parser.parse_args()
```

### Compress, decompress, checksum

```py
# Compute crc32 checksum
import zlib 
  
string = 'I want this checksum'

# using zlib.crc32() method 
checksum = zlib.crc32(s.encode())
checksum_1 = zlib.crc32(b"Also checksum of this.")

print(checksum, checksum_1) 
```
[python zlib](https://docs.python.org/3/library/zlib.html)

### underscored names in python


- `_single_leading_underscore`: weak "internal use" indicator. E.g. `from M import *` does not import objects whose names start with an underscore.
- `single_trailing_underscore_`: used by convention to avoid conflicts with Python keyword, e.g.
```py
tkinter.Toplevel(master, class_='ClassName')
```
- `__double_leading_underscore`: when naming a class attribute, invokes name mangling (inside `class FooBar`, `__boo` becomes `_FooBar__boo`; see below).

- `__double_leading_and_trailing_underscore__`: "magic" objects or attributes that live in user-controlled namespaces. E.g. `__init__`, `__import__` or `__file__`. Never invent such names; only use them as documented.

#### Dunders (double underscores)

```py
def getStuff(): return [1, "1", None, 4.5, {}];

def uniqueTypes():
    object_list = getStuff()
    return {type(x) for x in object_list}

# How to know if None was in object_list if we do not have it
types = uniqueTypes()
if None.__class__ in types:
    print("Function getStuff is corrupted, returns None while it should not")
```

### ctypes

[top source](https://www.auctoris.co.uk/2017/04/29/calling-c-classes-from-python-with-ctypes/)
[real pyhton c binding](https://realpython.com/python-bindings-overview/)
[read docu for c/python types](https://docs.python.org/3.6/library/ctypes.html)
[source 2](https://medium.com/@stephenscotttucker/interfacing-python-with-c-using-ctypes-classes-and-arrays-42534d562ce7)
[source 3](https://solarianprogrammer.com/2019/07/18/python-using-c-cpp-libraries-ctypes/)

```cpp
void c_fun(const char * bytes);
```

```py
c_fun("super unicode".encode())
```
[pass unicode as bytes](https://stackoverflow.com/questions/27285405/how-can-ctypes-be-used-to-parse-unicode-strings)

### Python 2 differences

#### Math in pyton2 doesn't work well
```
>>> 4**2
16
>>> 16**(1/2)
1
```
---