import turtle
import random
#e.ayar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle ile Desen Cizme")
t = turtle.Turtle()
t.speed(0) #enhizlicizimmodu
t.pensize(2)
#renklistesi
colors =["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
#deseniciz
for i in range(36):
    t.color(random.choice(colors))
    t.circle(100)
    t.left(10)


turtle.done()
