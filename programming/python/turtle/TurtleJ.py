#!/usr/bin/env python3

# import modulu
import turtle as t
import sys

# CONSTANTS
width, height = 1800, 1000
leng = 20
deg = 45
ang = 25
defClr = 'brown'
penSize = 3

# INITS
'''
ww, wh = t.window_height(), t.window_width()
ww_half = ww // 2
t.setworldcoordinates (-ww_half, 0, ww_half, ww)
'''

stack = []
t.screensize(width, height)
t.speed(0)
t.tracer(1000)

t.penup()
t.color(defClr)
t.pensize(penSize)
t.left(90)
#t.setposition(width/2, height)
t.setposition(0, -height/2)
t.pendown()

def showTree(s):
    for ch in s:
        if ch is '1':
            t.forward(leng)
        elif ch is '[':
            stack.append((t.pos(), t.heading()))
            t.left(deg)
        elif ch is ']':
            (p,h) = stack.pop()
            t.penup()
            t.setposition(p)
            t.pendown()
            t.setheading(h)
            t.right(deg)
        elif ch is '0':
            t.color('green')
            t.forward(leng)
            t.color(defClr)
    # hlavní GUI-smyčka (aby se okno nezavřelo samo od sebe)
    t.mainloop()
    # t.done()

def showPlant(s):
    for ch in s:
        if ch is 'F':
            t.forward(leng)
        if ch is '-':
            t.left(ang)
        if ch is '+':
            t.right(ang)
        elif ch is '[':
            stack.append((t.pos(), t.heading()))
        elif ch is ']':
            (p,h) = stack.pop()
            t.penup()
            t.setposition(p)
            t.setheading(h)
            t.pendown()

    # hlavní GUI-smyčka (aby se okno nezavřelo samo od sebe)
    t.mainloop()
    # t.done()

# AUTOMATS
# TREE
'''
variables : 0, 1
constants: [, ]
axiom : 0
rules : (1 → 11), (0 → 1[0]0)
'''
def tree(ch):
    if ch is '0':
        return '1[0]0'
    elif ch is '1':
        return '11'
    else:
        return ch
# PLANT
'''
variables : X F
constants : + − [ ]
start : X
rules : (X → F+[[X]-X]-F[-FX]+X), (F → FF)
angle : 25°
'''
def plant(ch):
    if ch is 'X':
        return 'F+[[X]-X]-F[-FX]+X'
    elif ch is 'F':
        return 'FF'
    else:
        return ch

def getNextGen(automat, sP):
    sN = ''
    fl = False

    for ch in sP:
        """
        fl = True if (ch is start) else False
        chN = automat(ch) if (fl) else ch
        """
        chN = automat(ch)
        sN += chN
    return sN

def p(key,value):
    print("{k} : {v}".format(k=key,v=value))


# MAIN 

# Tree
'''
s = '0'
gens = 8
automat = tree
viewer = showTree
'''
# Plant
s = 'X'
gens = int(sys.argv[1]) if(len(sys.argv) > 1) else 6
leng = int(sys.argv[2]) if(len(sys.argv) > 2) else 20
automat = plant
viewer = showPlant


for ii in range(gens):
    s = getNextGen(automat, s)
    print('s ' + str(ii) + ' ' + s)
    if (ii == gens-1):
        viewer(s)

'''
# nakreslení čtyř stran čtverce
for i in range(4):
    t.forward(100)
    t.left(90)
'''
 
'''
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()
'''

