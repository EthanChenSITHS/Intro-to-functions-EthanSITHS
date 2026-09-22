import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

# def square(x,turn): 
#     for i in range(4):
#         # i is an incrementor/iterator
#         t.forward(x)
#         t.left(turn)
# square(200,90)

# def triangle(x,turn): 
#     for i in range(3):
#         t.forward(x)
#         t.left(turn)
# triangle(200,120)

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

# """ sidelength = 100
# rotate = 90
# def square(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)
# square(sidelength,rotate)
#  """
# def doubleSquares(iRange):
#     length = 1
#     for i in range(iRange):
#         square(length, 90)
#         length = length * 2
# doubleSquares(10)

# def addSquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length, 90)
#         length += 25
# addSquares(5)
sidelength = 100
rotate = 144
def star(x,y):
    for i in range(10):
        t.forward(x)
        t.left(y)
star(sidelength,rotate)


def starsixty(iRange):
    length = 1 
    t.speed(5000)
    for i in range(iRange):
        star(length,144)
        length +=5 
        t.right(5)
starsixty(60)






