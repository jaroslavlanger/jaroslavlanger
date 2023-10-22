# XML

## TODO

* [SVG: Scalable Vector Graphics](https://developer.mozilla.org/en-US/docs/Web/SVG)

## What is xml

https://www.w3schools.com/xml/xml_whatis.asp

## XML comment 

https://www.tutorialspoint.com/xml/xml_comments.htm

## XML schema

https://www.w3schools.com/xml/schema_intro.asp

## Special characters

obviously as every enviroment, xml has also some characters requiring special treat, after every ampersand an semicolon is necessary
```
"   &quot;
'   &apos;
<   &lt;
>   &gt;
&   &amp;
```
[source](https://stackoverflow.com/questions/1091945/what-characters-do-i-need-to-escape-in-xml-documents)

## xpath

### syntax

**nodename** - Selects all nodes with the name "nodename"

**/** - Selects from the root node

**//** - Selects nodes in the document from the current node that match the selection no matter where they are

**.** - Selects the current node

**..** - Selects the parent of the current node

**@** - Selects attributes

**nodename[]** - propagation, selects all nodes, that fits condition inside of []

### examples

/bookstore/book[1]  Selects the first book element that is the child of the bookstore element.
Note: In IE 5,6,7,8,9 first node is[0], but according to W3C, it is [1]. To solve this problem in IE, set the SelectionLanguage to XPath:
```
/bookstore/book[last()-1]
```
Selects the last but one book element that is the child of the bookstore element

```
/bookstore/book[position()<3]
```
Selects the first two book elements that are children of the bookstore element

```
//title[@lang='en']
```
Selects all the title elements that have a "lang" attribute with a value of "en"

```
/bookstore/book[price>35.00]/title
```
Selects all the title elements of the book elements of the bookstore element that have a price element with a value greater than 35.00

[source](https://www.w3schools.com/xml/xpath_syntax.asp)
