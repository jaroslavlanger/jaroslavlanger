// https://jsantell.com/l-systems

// A-FRAME
var scene = document.getElementById('scene01');

// SUBFUNCTIONS
var drawLine = function(x0, y0, z0, x1, y1, z1, turnDeg, len){
    //console.log(x0, y0, x1, y1);
    x = x0 + (x1 - x0) / 2; // middle of x0 x1
    y = y0 + (y1 - y0) / 2; // middle of y0 y1
    z = z0 + (z1 - z0) / 2; // middle of z0 z1
    //console.log(x, y);
    turnDeg = turnDeg - 90; // rotation around z axis 0 means 90 turnDegrees in math
    
    let el = document.createElement('a-cylinder');
    
    //zPos = -3; // z position
    var position = '' + x + ' ' + y + ' ' + z;
    //console.log(position);
    el.setAttribute('position', position);
    el.setAttribute('height', len)

    rad = len/10; // radius is 1/20 of length
    el.setAttribute('radius', rad);
    el.setAttribute('color', 'green');
    
    var rotation = '0 0 ' + turnDeg;
    el.setAttribute('rotation',rotation);
    el.setAttribute('shadow');
    scene.appendChild(el);
}

// TURTLE
const Turtle = function(x=0, y=0, z=-3, tD=90, pD=0, rD=0, color='black'){
    //this.canvas = ctx.canvas;
    [this.X, this.Y, this.Z] = [x, y, z];
    this.turnDeg = tD;
    //console.log(this.turnDeg);
    this.turnRad = Math.PI*tD/180;
    console.log(Math.PI);
    console.log(this.turnRad, tD);
    this.pitchDeg = pD;
    this.pitchRad = Math.PI*pD/180;
    this.rollDeg = rD;
    this.rotation = Math.PI*rD/180;
    this.penIsDown = true;

    this.forward = function(length){
        //console.log(length, this.turnRad);
        newX = this.X + length*Math.cos(this.turnRad);
        newY = this.Y + length*Math.sin(this.turnRad);
        newZ = -3
        //console.log(this.turnRad,newX, newY);
        drawLine(this.X, this.Y, this.Z, newX, newY, newZ, this.turnDeg, length);
        [this.X, this.Y, this.Z] = [newX, newY, newZ];
    };
  
    this.left = function(turnDeg){
        this.turnRad = this.turnRad + Math.PI*turnDeg/180;
        this.turnDeg += turnDeg;
    };
  
    this.right = function(turnDeg){
        this.turnRad = this.turnRad - Math.PI*turnDeg/180;
        this.turnDeg -= turnDeg;
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
    this.setturnRad = function(h){
        this.turnRad = h;
        this.turnDeg = 180*h/Math.PI;
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
            this.stack.push([[t.X, t.Y],t.turnRad])
            break;
        case ']':
            [p, h] = this.stack.pop();
            t.penup();
            t.setposition(p[0], p[1]);
            t.setturnRad(h);
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
const step_length = 0.03;
const turn_angle = 25;
const start_angle = 90;
const color = 'darkgreen'
var t = new Turtle(0, 0, -3, start_angle, 0, 0, 'black');
var s = 'X';
var gens = 6;
var i;

for (i = 0; i < gens; i++) { 
    s = getNextGen(s);
    //console.log("generated string s", s)
    if (i == gens-1) {
        viewPlant(s, step_length, turn_angle);
    }
}