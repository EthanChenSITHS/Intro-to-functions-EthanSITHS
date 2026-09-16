import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

def square(): 
    for i in range(60):
        t.forward(100)
        t.left(5)

square()