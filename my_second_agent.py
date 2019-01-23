"""
Adapted from Think Python 2, by Allen Downey. Chapter 4
"""


import turtle


def square(agent, l):
    """ Receives a turtle and moves it in a square
        Specifically, not using for (yet)
    """

    agent.speed(3)

    for i in range(4):
        agent.fd(l)
        agent.lt(90)


def make_polygon(agent, l, n):
    angle = 360 / n
    for i in range(n):
        agent.fd(l)
        agent.lt(angle)


if __name__ == '__main__':
    maria = turtle.Turtle()
    jose = turtle.Turtle()
    maria.color('red')
    square(maria, 100)
    square(jose, 75)
    jose.penup()
    jose.setpos(-100, -100)
    jose.pendown()
    square(jose, -75)
    jose.color('green')
    jose.pensize(4)
    make_polygon(jose, 100, 6)
    maria.color('blue')
    maria.pensize(2)
    make_polygon(maria, 10, 36)
    turtle.mainloop()
