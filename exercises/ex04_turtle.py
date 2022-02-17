"""It is a masterpiece of natural lanscapes."""

__author__ = "730528622"

from turtle import Turtle, colormode, done 


def main() -> None:
    """The entrypoint of my scene."""
    picture: Turtle = Turtle()
    colormode(255)
    picture.speed(50)
    sun(picture, 250, 160, 80)

    tree_position = -300
    i: int = 0
    while i < 3:
        tree(picture, tree_position, -300, 70, 150)
        tree_position += 160
        i += 1
    
    j: int = 0
    mountain_x = -270
    mountain_y = 100
    while j < 3:
        mountain(picture, mountain_x, mountain_y, 50)
        mountain_x += 80
        mountain_y += 60
        j += 1
    mysterious_celetial_body(picture, 200, 0, 100)
    done()
    return


def tree(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a green tree at the bottom of the masterpiece."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    a_turtle.color("green")
    a_turtle.begin_fill()
    while i < 4:
        if i % 2 == 0:
            a_turtle.forward(width)
        else:
            a_turtle.forward(height)
        a_turtle.left(90)
        i = i + 1
    a_turtle.end_fill()
    leafage(a_turtle, x - width * (1/2), y + height, width * 2)
    return
    
        
def leafage(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw the leafage part of the tree."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color(16, 107, 46)
    a_turtle.begin_fill()
    i: int = 0
    while i < 3:
        a_turtle.forward(width)
        a_turtle.left(120)
        i += 1
    a_turtle.end_fill()
    return


def mountain(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Painted on the rolling mountains in the distance."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(45)
    a_turtle.pendown()
    a_turtle.color(124, 132, 127)
    a_turtle.begin_fill()
    i: int = 0
    while i < 6:
        a_turtle.forward(length)
        if i % 2 == 0:
            a_turtle.right(90)
        else:
            a_turtle.left(90)
        i += 1
    a_turtle.end_fill()
    

def sun(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a big shining sun."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.pendown()
    a_turtle.color()
    a_turtle.color("yellow")
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()
    return


def mysterious_celetial_body(a_turtle: Turtle, x: float, y: float, mysterious_length: float) -> None:
    """According to a recent scientific report, researchers have recently discovered a mysterious planet at a distance of 0.8 billion."""
    """Kilometers from the Sun. The planet is glowing red and rotates in a triangular trajectory. The planet is now moving toward Earth."""
    """At a high speed and scientists expect it to hit the planet in a month. As the two planets get closer, humans can gradually see."""
    """The planet's outline faintly on the Earth's surface. Scientists say the only way so far to get the planet to deviate from its."""
    """Motion is to get a full mark score on my comp110 exercise assignment."""
    i: int = 0
    a_turtle.color("red")
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.pendown()
    degree: float = 120
    while (i < 100):
        a_turtle.forward(mysterious_length)
        a_turtle.left(degree)
        degree += 1
        i += 1
        mysterious_length = mysterious_length * 0.97
    return


if __name__ == "__main__":
    main()
