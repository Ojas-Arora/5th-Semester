import turtle
def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(3, "blue") 
def draw_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r  
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("blue")
    turtle.hideturtle()
    turtle.tracer(0, 0)
    draw_point(xc + x, yc + y)
    draw_point(xc - x, yc + y)
    draw_point(xc + x, yc - y)
    draw_point(xc - x, yc - y)
    draw_point(xc + y, yc + x)
    draw_point(xc - y, yc + x)
    draw_point(xc + y, yc - x)
    draw_point(xc - y, yc - x)
    print(f"Point: ({xc + x}, {yc + y})")
    print(f"Point: ({xc - x}, {yc + y})")
    print(f"Point: ({xc + x}, {yc - y})")
    print(f"Point: ({xc - x}, {yc - y})")
    print(f"Point: ({xc + y}, {yc + x})")
    print(f"Point: ({xc - y}, {yc + x})")
    print(f"Point: ({xc + y}, {yc - x})")
    print(f"Point: ({xc - y}, {yc - x})")
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1
        x += 1
        draw_point(xc + x, yc + y)
        draw_point(xc - x, yc + y)
        draw_point(xc + x, yc - y)
        draw_point(xc - x, yc - y)
        draw_point(xc + y, yc + x)
        draw_point(xc - y, yc + x)
        draw_point(xc + y, yc - x)
        draw_point(xc - y, yc - x)
        print(f"Point: ({xc + x}, {yc + y})")
        print(f"Point: ({xc - x}, {yc + y})")
        print(f"Point: ({xc + x}, {yc - y})")
        print(f"Point: ({xc - x}, {yc - y})")
        print(f"Point: ({xc + y}, {yc + x})")
        print(f"Point: ({xc - y}, {yc + x})")
        print(f"Point: ({xc + y}, {yc - x})")
        print(f"Point: ({xc - y}, {yc - x})")
    turtle.update()
def main():
    xc, yc = 0, 0  
    r = 10 
    draw_circle(xc, yc, r)  
    turtle.done()  
if __name__ == "__main__":
    main()
