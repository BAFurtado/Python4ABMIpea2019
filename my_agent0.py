import turtle


def polygon(n, t):
    # n é o número de lados do poligono
    # t é o tamanho em passos do objeto
    b = turtle.Turtle()
    b.speed(1)
    for i in range(n):
        b.forward(t)
        b.lt(360/n)



if __name__ == '__main__':
    polygon(8, 75)
    turtle.mainloop()
