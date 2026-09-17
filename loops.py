import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

def square(x,turn): 
    for i in range(4):
        # i is an incrementor/iterator
        t.forward(x)
        t.left(turn)
square(200,90)

def triangle(x,turn): 
    for i in range(3):
        t.forward(x)
        t.left(turn)
triangle(200,120)

# def squaresixty():
#     t.speed(5000)
#     for i in range(60):
#         square(200,90)
#         t.right(5)
# squaresixty()

# def trianglesixty():
#     t.speed(5000)
#     for i in range(60):
#         triangle(200,120)
#         t.right(5)
# trianglesixty()

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(sidelength,rotate)

