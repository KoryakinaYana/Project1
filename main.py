#тут пишем команду
from turtle import *
#Yana-romb
def romb():

    down()
    forward(150)
    left(60)
    forward(150)
    left(120)
    forward(150)
    left(60)
    forward(150)
    mainloop()

def square(a):
    turtle.down()
    for _ in range(4):
        forward(a)
        right(90)
    up()
    mainloop()
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
romb()
# Grate
# Ok !turtle.up()
#     turtle.goto(-400,-300)
#svg
