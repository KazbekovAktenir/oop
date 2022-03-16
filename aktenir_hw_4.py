import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("red")
a, b = 0, 0
t.speed(0)
t.goto(0, 200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 220:
        break
    t.hideturtle()
turtle.done()
