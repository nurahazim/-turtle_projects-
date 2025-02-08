import turtle
#ekranolustur
screen = turtle.Screen()
screen.title("Turtle ile N Harfi Cizme")
screen.bgcolor("lightblue")
#turtle objesi
t = turtle.Turtle()
t.pensize(6)
t.speed(4)
t.pencolor("red")
t.fillcolor("yellow")
#"N" cizme
t.penup()
t.goto(-50, -100) #solaltnokta
t.pendown()
t.goto(-50, 100) #solustnokta
t.pencolor("green")
t.goto(50, -100) #sagaltnokta
t.pencolor("blue")
t.goto(50, 100)  #sagustnokta
#cizmi bitir
t.penup()
t.goto(0, 0)
t.pendown()
turtle.done()
