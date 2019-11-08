#тут пишем команду
from turtle import *

#Yana-romb
def romb():

    down()
    for _ in range (2):
        forward(z)
        left(60)
        forward(z)
        left(120)
    up()
    mainloop()

#Sonya-square
def square():
    turtle.down()
    for _ in range(4):
        forward(x)
        right(90)
    up()
    mainloop()

#Masha-triangle
def tria60(a):
    down()
    right(30)
    for _ in range(3):
        forward(y)
        right(120)
    up()
    mainloop()


# Grate
# Ok !turtle.up()
#     turtle.goto(-400,-300)
#svg
