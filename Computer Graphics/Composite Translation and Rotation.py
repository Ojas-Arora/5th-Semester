import turtle
import math

WIDTH, HEIGHT = 1000, 700
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("white")
screen.title("Composite Translation and Rotation with Turtle")

def draw_polygon(points, color):
    turtle.penup()
    turtle.goto(points[0][0], points[0][1])
    turtle.pendown()
    turtle.pencolor(color)
    for point in points[1:]:
        turtle.goto(point[0], point[1])
    turtle.goto(points[0][0], points[0][1])

def print_text(text, position, font_size=15, color="black"):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.write(text, align="center", font=("Arial", font_size, "normal"))

def draw_corner_points(points, color="black"):
    turtle.penup()
    for x, y in points:
        turtle.goto(x, y)
        turtle.dot(5, color)
        turtle.goto(x, y + 15)
        turtle.pendown()
        turtle.write(f"({x}, {y})", align="center", font=("Arial", 10, "normal"))
        turtle.penup()

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
    return math.floor(xnew + cx), math.floor(ynew + cy)

def composite_translation(points, translations):
    return [translate_point(x, y, translations[0], translations[1]) for x, y in points]

def composite_rotation(points, cx, cy, angle):
    return [rotate_point(x, y, cx, cy, angle) for x, y in points]

def draw_shapes():
    turtle.speed(0)
    turtle.hideturtle()

    start_x = -400
    y_positions = [250, -50, -250]
    
    triangle = [(-400, 200), (-350, 100), (-450, 100)]
    rectangle = [(-200, 200), (-100, 200), (-100, 50), (-200, 50)]
    
    print_text("Original Shapes", (start_x, y_positions[0]))  
    draw_polygon(triangle, "blue")
    draw_polygon(rectangle, "blue")
    draw_corner_points(triangle, color="blue")
    draw_corner_points(rectangle, color="blue")
    
    translations = (500, 0)
    print_text("Composite Translation", (start_x + 500, y_positions[0])) 
    
    translated_triangle = composite_translation(triangle, translations)
    translated_rectangle = composite_translation(rectangle, translations)
    
    draw_polygon(translated_triangle, "green")
    draw_polygon(translated_rectangle, "green")
    draw_corner_points(translated_triangle, color="green")
    draw_corner_points(translated_rectangle, color="green")

    rotation_center_triangle = (-350, 150)
    rotation_center_rectangle = (-150, 125)
    angles = 45
    
    print_text("Composite Rotation", (start_x + 200, y_positions[1] + 50))  
    
    rotated_triangle = composite_rotation(triangle, rotation_center_triangle[0], rotation_center_triangle[1], angles)
    rotated_rectangle = composite_rotation(rectangle, rotation_center_rectangle[0], rotation_center_rectangle[1], angles)
    
    rotated_triangle_shifted = composite_translation(rotated_triangle, (0, -300))
    rotated_rectangle_shifted = composite_translation(rotated_rectangle, (0, -300))

    draw_polygon(rotated_triangle_shifted, "red")
    draw_polygon(rotated_rectangle_shifted, "red")
    draw_corner_points(rotated_triangle_shifted, color="red")
    draw_corner_points(rotated_rectangle_shifted, color="red")

    turtle.hideturtle()
draw_shapes()
turtle.done()
