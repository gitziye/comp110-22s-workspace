from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()


leo.penup()
leo.goto(0, 30)
leo.pendown()
leo.fillcolor("grey")
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.forward(100)

done()