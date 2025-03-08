import turtle
def write_label(label, position):
    turtle.penup()
    turtle.goto(position[0], position[1] + 50)  
    turtle.pendown()
    turtle.write(label, align="center", font=("Arial", 14, "bold"))
    turtle.penup()

def draw_shape(vertices, position_offset=(0, 0)):
    turtle.penup()
    turtle.goto(vertices[0][0] + position_offset[0], vertices[0][1] + position_offset[1])
    turtle.pendown()
    for vertex in vertices[1:]:
        turtle.goto(vertex[0] + position_offset[0], vertex[1] + position_offset[1])
    turtle.goto(vertices[0][0] + position_offset[0], vertices[0][1] + position_offset[1])

def reflect_diagonal(vertices):
    return [(y, x) for x, y in vertices]

turtle.speed(2)
turtle.bgcolor("white")

pentagon_vertices = [(-50, 0), (-30, 50), (0, 70), (30, 50), (50, 0)]
rectangle_vertices = [(-50, -50), (-50, 50), (50, 50), (50, -50)]

gap_x = 300  
gap_y = 200  

turtle.color("black")
write_label("Original Pentagon", (-400, 100))
draw_shape(pentagon_vertices, position_offset=(-400, 50))

write_label("Original Rectangle", (-400, -50))
draw_shape(rectangle_vertices, position_offset=(-400, -100))

reflected_pentagon_diagonal = reflect_diagonal(pentagon_vertices)
reflected_rectangle_diagonal = reflect_diagonal(rectangle_vertices)

turtle.color("blue")
write_label("Reflection About Diagonal y=x (Pentagon)", (-400 + gap_x, 100))
draw_shape(reflected_pentagon_diagonal, position_offset=(-400 + gap_x, 100))

turtle.color("green")
write_label("Reflection About Diagonal y=x (Rectangle)", (-400 + gap_x, -50))
draw_shape(reflected_rectangle_diagonal, position_offset=(-400 + gap_x, -100))

turtle.hideturtle()
turtle.done()
