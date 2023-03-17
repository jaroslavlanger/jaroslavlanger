# Canvas

`2021 Jan 10, Jaroslav Langer`

## Contents

- [Accessing trough context](#accessing-trough-context)
- [Canvas offset](#canvas-offset)
- [Buttons](#buttons)
- [Drawing](#drawing)
  - [Circle](#circle)
  - [Line](#line)
- [Canvas properties](#canvas-properties)
  - [Widht and height](#widht-and-height)
  - [Baground colour](#baground-colour)
  - [Line width](#line-width)
  - [Line color](#line-color)

## Accessing trough context

```js
var canvas = document.getElementById('cnvs01');
var ctx = canvas.getContext('2d');

ctx.ANYTHING(...)
```

## Canvas offset

```js
var rect = event.target.getBoundingClientRect();
var x = event.pageX - rect.left;
var y = event.pageY - rect.top;
```

## Buttons

```js
if(event.buttons>0)
    ctx.fillRect(x, y, 5, 5);
```

- [buttons (mozilla.org)](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/buttons)

## Drawing

### Circle 

```js
ctx.drawCircle = function(x, y, r){
        this.beginPath();
        this.arc(x, y, r, 0, 2*Math.PI);
        this.fill();
    }
```

### Line

```js
ctx.drawLine = function(x, y){
    this.beginPath();
    this.moveTo(window.prevX, window.prevY);
    this.lineTo(x, y);
    this.stroke();
}
```

- [draw a line](https://www.w3schools.com/tags/canvas_lineto.asp)
- [line tutorial](https://www.html5canvastutorials.com/tutorials/html5-canvas-line-color/)

## Canvas properties

### Widht and height

```js
[canvas.width, canvas.height] = [window.innerWidth, window.innerHeight];
```

### Baground colour

```js
canvas.style.backgroundColor = 'lightblue';
```

### Line width

```js
ctx.lineWidth = 50;
```

### Line color

```js
var changeColor = function(color){
    ctx.strokeStyle = color;
}
```

