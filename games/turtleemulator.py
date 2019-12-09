# Turtle emulator in Python

import sys, os, math, random, functools
import numpy as np

import matplotlib
import matplotlib.pyplot as pp
import matplotlib.animation as anim

#matplitlib inline
from IPython.display import display,HTML



class Terrarium(object):
    def __init__(self):
        self.fig = pp.figure(figsize=(3,3))
        self.axes = pp.axes()

        self.axes.set_xticks([])
        self.axes.set_yticks([])

        for spine in ['bottom','top','left','right']:
            self.axes.spines[spine].set_color('0.9')

    def rescale(self):
        self.axes.axis('scaled')

        xmin, xmax, ymin, ymax = self.axes.axis()
        dx = (xmax - xmin) / 50
        self.axes.axis([xmin-dx,xmax+dx,ymin-dx,ymax+dx])        


class Turtle(object):
    deg = math.pi / 180.0
    
    def __init__(self,terrarium):
        self.pos = (0,0)
        self.angle = 0
        self.pen = True
        
        self.axes = terrarium.axes
    
    def forward(self,distance):
        posnew = (self.pos[0] + distance * math.cos(self.deg * self.angle),
                  self.pos[1] + distance * math.sin(self.deg * self.angle))
    
        if self.pen:
            line = pp.Line2D((self.pos[0],posnew[0]),(self.pos[1],posnew[1]))
            self.axes.add_line(line)
        
        self.pos = posnew
    
    def back(self,distance):
        self.forward(-distance)
    
    def left(self,angle):
        self.angle = (self.angle + angle) % 360
    
    def right(self,angle):
        self.angle = (self.angle - angle) % 360
    
    def penup(self):
        self.pen = False
    
    def pendown(self):
        self.pen = True



t = Terrarium()

t1 = Turtle(t)

t1.forward(100)
t1.left(90)
t1.forward(150)
t1.right(45)
t1.back(100)

t.rescale()
