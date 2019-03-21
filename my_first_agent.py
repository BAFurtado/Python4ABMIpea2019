"""
Adapted from Think Python 2, by Allen Downey. Chapter 4
"""

import turtle


def square(my_agent):
    """ Receives a turtle and moves it in a square
        Specifically, not using for (yet)
    """
    my_agent.speed(3)
    my_agent.fd(100)
    my_agent.lt(90)
    my_agent.fd(100)
    my_agent.lt(90)
    my_agent.fd(100)
    my_agent.lt(90)
    my_agent.fd(100)


def dif_square(my_agent, x, y):
    """ Receives a turtle, moves to a fixed position and draws a square in red"""
    my_agent.speed(1)
    my_agent.color('green')
    my_agent.pensize(2)
    my_agent.penup()
    my_agent.setpos(x, y)
    my_agent.pendown()
    square(my_agent)


if __name__ == '__main__':
    tuga = turtle.Turtle()
    for i in range(4):
        dif_square(tuga, 20 * i, 20 * i)
    turtle.mainloop()

