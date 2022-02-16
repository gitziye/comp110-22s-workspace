from turtle import Turtle, colormode, done
bob: Turtle = Turtle()

bob.color("black")
bob.penup()
bob.goto(45, 60)
bob.pendown()

bob.speed(50)

i: int = 0
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i = i + 1

side_length = 300

i: int = 0
while (i < 200):
    bob.forward(side_length)
    bob.left(122)
    i = i + 1
    side_length = side_length * 0.98

done()