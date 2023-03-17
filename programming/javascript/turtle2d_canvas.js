// CANVAS
var canvas = document.getElementById('cnvs01');
var context = canvas.getContext('2d');
[canvas.width, canvas.height] = [window.innerWidth, window.innerHeight];
canvas.style.backgroundColor = 'lightblue';

// SUBFUNCTIONS
context.drawLine = function(x0, y0, x1, y1){
    this.beginPath();
    this.moveTo(x0, y0);
    this.lineTo(x1, y1);
    this.stroke();
}

// TURTLE
const Turtle = function(ctx, h=90, x=window.innerWidth/2, y=window.innerHeight/2){
    this.canvas = ctx.canvas;
    [this.X, this.Y] = [x, y];
    this.heading = Math.PI*h/180;
    this.penIsDown = true;

    this.forward = function(length){
        newX = this.X + length*Math.cos(this.heading);
        newY = this.Y - length*Math.sin(this.heading);
        ctx.drawLine(this.X, this.Y, newX, newY);
        [this.X, this.Y] = [newX, newY];
    };

    this.left = function(deg){
        this.heading = this.heading + Math.PI*deg/180;
    };

    this.right = function(deg){
        this.heading = this.heading - Math.PI*deg/180;
    };

    this.penup = function(){
        this.penIsDown = false;
    };
    this.pendown = function(){
        this.penIsDown = true;
    };
    this.setposition = function(x, y){
        [this.X, this.Y] = [x, y];
    };
    this.setheading = function(h){
        this.heading = h;
    };
};

// PLANT
var viewPlant = function(s, step, angle){
    var len = s.length;
    this.stack = [];

    for (k = 0; k < len; k++) {
        switch (s.charAt(k)) {
        case 'F':
            t.forward(step);
            break;
        case '-':
            t.left(angle);
            break;
        case '+':
            t.right(angle);
            break;
        case '[':
            this.stack.push([[t.X, t.Y],t.heading])
            break;
        case ']':
            [p, h] = this.stack.pop();
            t.penup();
            t.setposition(p[0], p[1]);
            t.setheading(h);
            t.pendown();
            break;
        default:
            if(s.charAt(k) != 'X'){
                alert('INVALID CHARACTER OCCURED!');
            }
        }
    }
}

var plant = function(ch){
    switch(ch) {
    case 'X':
        return 'F+[[X]-X]-F[-FX]+X'
    case 'F':
        return 'FF'
    default:
        return ch;
    }
}

var getNextGen = function(sP){
    var sN = '';
    var len = sP.length;
    for (j = 0; j < len; j++) { 
        sN += plant(sP.charAt(j));
    }
    return sN;
}

// MAIN
const step_length = 1;
const turn_angle = 25;
const start_angle = 145;
var t = new Turtle(context, start_angle, window.innerWidth*(9/10), window.innerHeight*(19/20));

var s = 'X';
var gens = 9;
var i;
context.strokeStyle = 'darkgreen';
for (i = 0; i < gens; i++) { 
    s = getNextGen(s);
    //console.log(s);
    if (i == gens-1) {
        viewPlant(s, step_length, turn_angle);
    }
}
