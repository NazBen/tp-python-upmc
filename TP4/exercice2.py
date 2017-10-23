import turtle
import math

def move(p1, p2):
    """
    """
    v_x = p2[0] - p1[0]
    v_y = p2[1] - p1[1]
    angle = math.atan2(v_y, v_x)
    angle *= 180 / math.pi
    dist = math.sqrt(v_x**2 + v_y**2)
    return angle, dist

def get_middle(p1, p2):

    x = (p2[0] - p1[0]) / 2. + p1[0]
    y = (p2[1] - p1[1]) / 2. + p1[1]

    pm = [x, y]
    return pm

def triangle(a, b, c, niveau):
    """
    Parameters
    ----------
    """
    tutu = turtle.Turtle()
    tutu.hideturtle()
    prev_angle = 0
    for lvl in range(niveau+1):
        tutu.goto(*a)
        print (a, b, c)
        for elements in [[a, b], [b, c], [c, a]]:
            angle, dist = move(*elements)
            tutu.left(angle - prev_angle)
            tutu.forward(dist)
            prev_angle = angle

        a_new = get_middle(a, b)
        b_new = get_middle(b, c)
        c_new = get_middle(c, a)
        a, b, c = a_new, b_new, c_new
    
a = [0, 0]
b = [100, 0]
c = [0, 100]
niveau = 3
triangle(a, b, c, niveau)

turtle.exitonclick()