import turtle

win = turtle.Screen()
win.title("Mercedes Benz")
win.bgcolor(("black"))

t = turtle.Turtle()
t.speed(3)
circleRadius = 200
t.pencolor("silver")
t.pensize(3)
t.penup()
t.setposition(0, -150)
t.pendown()
t.circle(circleRadius)
t.penup()
t.left(90)
t.forward(circleRadius)
t.pendown()
t.forward(circleRadius)
t.penup()
t.right(180)
t.forward(circleRadius)
t.right(60)
t.pendown()
t.forward(circleRadius)
t.penup()
t.right(180)
t.forward(circleRadius)
t.right(60)
t.pendown()
t.forward(circleRadius)
t.penup()
t.speed(1)
t.right(180)
t.forward(200)
t.right(60)


