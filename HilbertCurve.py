from turtle import Turtle, mainloop

ANGLE = 90
DISTANCE = 10

def r_rule(turtle, n):
    if n < 1:
        return

    turtle.right(ANGLE)
    l_rule(turtle, n-1)
    turtle.forward(DISTANCE)
    turtle.left(ANGLE)
    r_rule(turtle, n - 1)
    turtle.forward(DISTANCE)
    r_rule(turtle, n-1)
    turtle.left(ANGLE)
    turtle.forward(DISTANCE)
    l_rule(turtle, n-1)
    turtle.right(ANGLE)


def l_rule(turtle, n):
    if n < 1:
        return

    turtle.left(ANGLE)
    r_rule(turtle, n-1)
    turtle.forward(DISTANCE)
    turtle.right(ANGLE)
    l_rule(turtle, n - 1)
    turtle.forward(DISTANCE)
    l_rule(turtle, n-1)
    turtle.right(ANGLE)
    turtle.forward(DISTANCE)
    r_rule(turtle, n-1)
    turtle.left(ANGLE)

def main():
    boss_turtle = Turtle()
    boss_turtle.speed("fastest")
    l_rule(boss_turtle, 2)
    boss_turtle.forward(DISTANCE)


if __name__ == '__main__':
    main()
    mainloop()
