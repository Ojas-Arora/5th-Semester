import turtle
import time
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def drawLineDDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1    
    if dx == 0:
        slope = float('inf')  
    elif dy == 0:
        slope = 0  
    else:
        slope = dy / dx   
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xinc = dx / steps
    Yinc = dy / steps
    x = x1
    y = y1
    points = []    
    for _ in range(steps + 1):
        turtle.goto(round(x), round(y))
        turtle.dot(3, "black")
        points.append(Point(round(x), round(y)))
        x += Xinc  
        y += Yinc   
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
    drawLineDDA(x1, y1, x2, y2)   
    time.sleep(2) 
    turtle.clear()
    x1, y1 = 50, 50
    x2, y2 = 100, 100
    drawLineDDA(x1, y1, x2, y2)
    time.sleep(2)  
    turtle.clear()
    x1, y1 = 100, 100
    x2, y2 = 50, 60
    drawLineDDA(x1, y1, x2, y2)  
    turtle.hideturtle()
    turtle.done()
if __name__ == "__main__":
    main()
