# Translation and Rotation of Shapes
import turtle
import math
WIDTH, HEIGHT = 1000, 700
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("white")
screen.title("Shapes Drawing with Turtle")
def draw_polygon(points, color):
    turtle.penup()
    turtle.goto(points[0][0], points[0][1])
    turtle.pendown()
    turtle.pencolor(color)
    for point in points[1:]:
        turtle.goto(point[0], point[1])
    turtle.goto(points[0][0], points[0][1])
def translate_point(x, y, tx, ty):
    return x + tx, y + ty
def rotate_point(x, y, cx, cy, angle):
    rad = math.radians(angle)
    s = math.sin(rad)
    c = math.cos(rad)
    x -= cx
    y -= cy
    xnew = x * c - y * s
    ynew = x * s + y * c
    x = xnew + cx
    y = ynew + cy
    return x, y
def print_text(text, position, font_size=15, color="black"):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.write(text, align="center", font=("Arial", font_size, "normal"))
def draw_shapes():
    turtle.speed(0)
    turtle.hideturtle()
    start_x = -400
    y_positions = [250, -50] 
    print_text("Original Shapes", (start_x, y_positions[0]))  
    triangle = [(-400, 200), (-350, 100), (-450, 100)]  
    rectangle = [(-200, 200), (-100, 200), (-100, 50), (-200, 50)]  
    draw_polygon(triangle, "blue")
    draw_polygon(rectangle, "blue")
    print_text("After Rotation", (start_x + 450, y_positions[0]), color="blue")  
    rotated_triangle = [rotate_point(x, y, -350, 150, 45) for x, y in triangle]
    rotated_rectangle = [rotate_point(x, y, -150, 150, 45) for x, y in rectangle]
    rotated_triangle = [translate_point(x, y, 500, 0) for x, y in rotated_triangle]
    rotated_rectangle = [translate_point(x, y, 500, 0) for x, y in rotated_rectangle]
    draw_polygon(rotated_triangle, "green")
    draw_polygon(rotated_rectangle, "green")
    print_text("After Translation", (start_x + 450, y_positions[1] + 50), color="blue")  # Moved further up
    translated_triangle = [translate_point(x, y, 500, -250) for x, y in triangle]  # Adjusted translation
    translated_rectangle = [translate_point(x, y, 500, -250) for x, y in rectangle]  # Adjusted translation
    draw_polygon(translated_triangle, "red")
    draw_polygon(translated_rectangle, "red")
    turtle.hideturtle()
draw_shapes()
turtle.done()
