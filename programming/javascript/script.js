var range = document.getElementById('range');

var output = document.getElementById('output');

var button = document.getElementById('button');

var value = document.getElementById('value');

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

var rangeHandler = function(evt) {
    value.innerHTML = range.value;
    
}

var buttonHandler = function(evt) {
    output.value = getRandomInt(range.value);
}

range.onchange = rangeHandler;

button.onclick = buttonHandler;

console.log(button);
