# JavaScript

JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions.

## References

* <https://developer.mozilla.org/en-US/docs/Web/JavaScript>

## TODO

Stačí napsat tohle, a pak to umí každé vytvořené pole.
```
Array prototype valueIn = function()
```

## Run JavaScript

* Run javascript in browser console (Ctrl+Shift+I).
* Install <https://nodejs.org/> javascript runtime environment.

## Node.js Package Managers

* [npm](https://www.npmjs.com/) is the default package manager for the Node.js maintained by npm, Inc a subsidiary of GitHub / Microsoft.
* [yarn](https://yarnpkg.com/) is one of the main javascript package managers, developed in 2016 by Sebastian McKenzie of Meta.

## Printing

Alert, blocks anything.

```js
alert('POP-UP MESSAGE!');
```

Write to log, great for debugging.

```js
console.log(total, typeof total);
```

## Variables

Best way for variables is keyword `var`.

```js
var name = 0;
```

Global variable.

```js
[window.prevX, window.prevY] = [ x, y ];
```

* [source](https://www.javatpoint.com/javascript-global-variable)
* [scope of variables](https://www.sitepoint.com/demystifying-javascript-variable-scope-hoisting/)

## Data types

### String

Length

```js
myString.length
```

**Concatenate strings**

```js
var hello = 'hell' + 'o';
// be careful
var fivety = '5' + 0; // will be '50'
```

**Accessing chars of string**

(like myString[i] in other languages)

```js
myString.charAt(i);
```

### Arrays

```js
var arr = [6,6,7];
```

**Number of items**

```js
myArray.length
```

### Adding item to array

```js
myArray.push("something");
```

* [source](https://www.w3schools.com/js/js_arrays.asp)

### Pop last item

```js
item = myArray.pop();
```

## Conditions

Switch

```js
switch (clicked%4) {
case 0:
    break;
case 1:
    clicked++;
    break;
default:
    clicked = 0;
}
```

* [source](https://www.w3schools.com/js/js_switch.asp)

## Loops

```js
var i;
for (i = 0; i < cars.length; i++) { 
  text += cars[i] + "<br>";
}
```

* [source](https://www.w3schools.com/js/js_loop_for.asp)

For loop i is key, not value

```js
for (var i in arr) {
    total = total + i;
}
```

## Functions

```js
var x = myFunction(4, 3);   // Function is called, return value will end up in x

function myFunction(a, b) {
  return a * b;             // Function returns the product of a and b
}
```

* [source](https://www.w3schools.com/js/js_functions.asp)

## HTML elements

Reference to DOM-object of element '<div id="odstavec">' from page.

```js
var canvas = document.getElementById('canvas01');
```

* https://www.w3schools.com/jsref/dom_obj_body.asp

Get root DOM object

```js
var outputElement = document.documentElement;
```

vložení připraveného HTML-fragmentu do cílového místa

```js
outputElement.innerHTML = txt;
```

### Append child

* https://www.w3schools.com/jsref/met_node_appendchild.asp

## Create element specify class

* https://www.htmldog.com/guides/javascript/advanced/creatingelements/

### Insert html string to element not replace

```js
element.insertAdjacentHTML(position, text);
```

* [source](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML)

## Handlers

### function handling action, gets event, which called it

```js
var onclickHandler = function(evt) {
    console.log('Click on <div id="odstavec">:', evt);
};
```

### Connects event with handler

```js
outputElement.onclick = onclickHandler;
```

### Access target from event

```js
evt.target.style.backgroundColor = 'yellow';
```

### Handeling general touch 

* [Pointer](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events)

### On touch screen

* [touch](https://www.w3schools.com/jsref/obj_touchevent.asp)
* [Touch events](https://developer.mozilla.org/en-US/docs/Web/API/Touch_events/Using_Touch_Events)

## Coordinates

```js
var actionDown = function(evt){
    console.log('clientX/Y: ', evt.clientX, evt.clientY );
    console.log('layerX/Y: ', evt.layerX, evt.layerY );
    console.log('pageX/Y: ', evt.pageX, evt.pageY );
    console.log('x/y', evt.x, evt.y );
    console.log("---------------------");
}
```

## Math

### Radians from degrees

```js
rad = Math.PI * deg/180;
```

### Trigonometric functions


```js
newX = this.X + length * Math.cos(this.heading);
newY = this.Y - length * Math.sin(this.heading);
```
