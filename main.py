#тут пишем команду
import turtle
def romb():
    import turtle
    turtle.down()
    turtle.forward(150)
    turtle.left(60)
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(150)
    turtle.left(60)
    turtle.forward(150)
    turtle.mainloop()
from turtle import *
def square():
    turtle.down()
    for _ in range(4):
        turtle.forward(150)
        turtle.right(90)
    turtle.up()
    turtle.mainloop()
def tria60():
    down()
    right(30)
    for _ in range(3):
        forward(150)
        right(120)
    up()
    mainloop()
def tria60big():
    down()
    right(30)
    for _ in range(3):
        forward(300)
        right(120)
    up()
    mainloop()
turtle.right(30)
tria60big()
# Grate
# Ok !turtle.up()
#     turtle.goto(-400,-300)
