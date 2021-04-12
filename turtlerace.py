from turtle import Turtle
from random import randint
mani = Turtle()
gaurav = Turtle()
ankit = Turtle()
dilip = Turtle()

mani.color('green')
mani.shape('turtle')
mani.penup()
mani.goto(-160, 100)
mani.pendown()

gaurav.color('red')
gaurav.shape('turtle')
gaurav.penup()
gaurav.goto(-160, 70)
gaurav.pendown()

ankit.color('blue')
ankit.shape('turtle')
ankit.penup()
ankit.goto(-160, 50)
ankit.pendown()

dilip.color('purple')
dilip.shape('turtle')
dilip.speed(4)
dilip.penup()
dilip.goto(-160, 30)
dilip.pendown()

for movement in range(100):
    mani.forward(randint(1,5))
    gaurav.forward(randint(1,5))
    ankit.forward(randint(1,5))
    dilip.forward(randint(1,5))
