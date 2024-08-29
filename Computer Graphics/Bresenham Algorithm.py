import turtle
import time
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def drawLineBresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy
    slope = dy / dx if dx != 0 else float('inf')  
    points = []
    x, y = x1, y1
    while True:
        turtle.goto(x, y)
        turtle.dot(3, "black")
        points.append(Point(x, y))
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy  
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.dot(10, "red")
    turtle.write(f"Start ({x1}, {y1})", font=("Arial", 8, "normal"))
    turtle.goto(x2, y2)
    turtle.dot(10, "blue")
    turtle.write(f"End ({x2}, {y2})", font=("Arial", 8, "normal"))
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    offset_x = 40  
    offset_y = 40  
    if slope > 1:
        turtle.goto(mid_x - offset_x, mid_y + offset_y)
        turtle.write("Slope > 1", font=("Arial", 12, "bold"))
    elif slope == 1:
        turtle.goto(mid_x + offset_x, mid_y + offset_y)
        turtle.write("Slope = 1", font=("Arial", 12, "bold"))
    elif slope == 0:
        turtle.goto(mid_x + offset_x, mid_y + offset_y)
        turtle.write("Slope = 0", font=("Arial", 12, "bold"))
    elif slope < 0:  
        turtle.goto(mid_x + offset_x, mid_y - offset_y)
        turtle.write("Slope < 0", font=("Arial", 12, "bold"))
    else:  
        turtle.goto(mid_x + offset_x, mid_y - offset_y)
        turtle.write("Slope < 1", font=("Arial", 12, "bold"))
def main():
    turtle.speed(0)
    turtle.penup()
    x1, y1 = 50, 50
    x2, y2 = 60, 100
    drawLineBresenham(x1, y1, x2, y2)   
    time.sleep(2)  
    turtle.clear()
    x1, y1 = 50, 50
    x2, y2 = 100, 100
    drawLineBresenham(x1, y1, x2, y2)
    time.sleep(2)  
    turtle.clear()
    x1, y1 = 100, 100
    x2, y2 = 50, 60
    drawLineBresenham(x1, y1, x2, y2)
    turtle.hideturtle()
    turtle.done()
if __name__ == "__main__":
    main()
