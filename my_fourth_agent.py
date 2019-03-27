"""
Adapted from Think Python 2, by Allen Downey. Chapter 4
"""

import turtle
import random


def make_polygon(agent, l, n):
    angle = 360 / n
    for i in range(n):
        agent.fd(l)
        agent.lt(angle)


def move(agent, a, b):
    return agent.setpos(a, b)


if __name__ == '__main__':

    gerson = turtle.Turtle()
    esa = turtle.Turtle()
    sissi = turtle.Turtle()
    marlene = turtle.Turtle()
    colors = ['red', 'green', 'purple', 'blue']
    agentes = [esa, gerson, marlene, sissi]
    for i in range(3):
        for k, i in enumerate(agentes):
            i.penup()
            i.setpos(random.randint(0, 100), random.randint(0, 120))
            i.pendown()
            i.color(colors[k])
            make_polygon(i, random.randint(40, 79), random.randint(3, 7))

    turtle.mainloop()
