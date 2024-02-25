# Mid point Ellipse Algorithm in Python
import turtle
def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(3, "blue")
def draw_ellipse(xc, yc, a, b):
    x = 0
    y = b
    d1 = (b**2) - (a**2 * b) + (0.25 * a**2) 
    draw_point(xc + x, yc + y)
    draw_point(xc - x, yc + y)
    draw_point(xc + x, yc - y)
    draw_point(xc - x, yc - y)
    print(f"Point: ({xc + x}, {yc + y})")
    print(f"Point: ({xc - x}, {yc + y})")
    print(f"Point: ({xc + x}, {yc - y})")
    print(f"Point: ({xc - x}, {yc - y})")
    while (a**2 * (y - 0.5)) > (b**2 * x):
        if d1 < 0:
            d1 = d1 + (b**2 * (2 * x + 3))
        else:
            d1 = d1 + (b**2 * (2 * x + 3)) + (a**2 * (-2 * y + 2))
            y -= 1
        x += 1
        draw_point(xc + x, yc + y)
        draw_point(xc - x, yc + y)
        draw_point(xc + x, yc - y)
        draw_point(xc - x, yc - y)
        if x % 5 == 0:  
            print(f"Point: ({xc + x}, {yc + y})")
            print(f"Point: ({xc - x}, {yc + y})")
            print(f"Point: ({xc + x}, {yc - y})")
            print(f"Point: ({xc - x}, {yc - y})")
    d2 = (b**2) * (x + 0.5)**2 + (a**2) * (y - 1)**2 - (a**2) * (b**2)  
    while y >= 0:
        if d2 > 0:
            d2 = d2 + (a**2 * (-2 * y + 3))
        else:
            d2 = d2 + (a**2 * (-2 * y + 3)) + (b**2 * (2 * x + 2))
            x += 1
        y -= 1
        draw_point(xc + x, yc + y)
        draw_point(xc - x, yc + y)
        draw_point(xc + x, yc - y)
        draw_point(xc - x, yc - y)
        if y % 5 == 0:  
            print(f"Point: ({xc + x}, {yc + y})")
            print(f"Point: ({xc - x}, {yc + y})")
            print(f"Point: ({xc + x}, {yc - y})")
            print(f"Point: ({xc - x}, {yc - y})")
    turtle.update()
def main():
    xc, yc = 0, 0  
    a, b = 50, 30  
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("blue")
    turtle.hideturtle()
    turtle.tracer(0, 0)
    draw_ellipse(xc, yc, a, b)
    turtle.done()
if __name__ == "__main__":
    main()
