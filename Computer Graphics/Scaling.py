import turtle
def write_label(label, position):
    turtle.penup()
    turtle.goto(position[0], position[1] + 50)  
    turtle.pendown()
    turtle.write(label, align="center", font=("Arial", 14, "bold"))
    turtle.penup()
def draw_triangle(vertices, position_offset=(0, 0)):
    turtle.penup()
    turtle.goto(vertices[0][0] + position_offset[0], vertices[0][1] + position_offset[1])
    turtle.pendown()
    for vertex in vertices[1:]:
        turtle.goto(vertex[0] + position_offset[0], vertex[1] + position_offset[1])
    turtle.goto(vertices[0][0] + position_offset[0], vertices[0][1] + position_offset[1])
def draw_rectangle(vertices, position_offset=(0, 0)):
    turtle.penup()
    turtle.goto(vertices[0][0] + position_offset[0], vertices[0][1] + position_offset[1])
    turtle.pendown()
    for vertex in vertices[1:]:
        turtle.goto(vertex[0] + position_offset[0], vertex[1] + position_offset[1])
    turtle.goto(vertices[0][0] + position_offset[0], vertices[0][1] + position_offset[1])
def scale_shape(vertices, Sx, Sy):
    return [(x * Sx, y * Sy) for x, y in vertices]
turtle.speed(2)
turtle.bgcolor("white")
triangle_vertices = [(-100, 0), (0, 100), (100, 0)]
rectangle_vertices = [(-50, -50), (-50, 50), (50, 50), (50, -50)]
gap_x = 250 
gap_y = 200  
turtle.color("black")
write_label("Original Triangle", (-400, 100))
draw_triangle(triangle_vertices, position_offset=(-400, 50))
write_label("Original Rectangle", (-400, -50))
draw_rectangle(rectangle_vertices, position_offset=(-400, -100))
scaled_triangle = scale_shape(triangle_vertices, 0.5, 0.5)
scaled_rectangle = scale_shape(rectangle_vertices, 0.5, 0.5)
turtle.color("blue")
write_label("Scaled Down (Triangle)", (-400 + gap_x, 100))
draw_triangle(scaled_triangle, position_offset=(-400 + gap_x, 50))
turtle.color("green")
write_label("Scaled Down (Rectangle)", (-400 + gap_x, -50))
draw_rectangle(scaled_rectangle, position_offset=(-400 + gap_x, -100))
scaled_triangle = scale_shape(triangle_vertices, 1.5, 1.5)
scaled_rectangle = scale_shape(rectangle_vertices, 1.5, 1.5)
turtle.color("red")
write_label("Scaled Up (Triangle)", (-400 + 2 * gap_x, 100))
draw_triangle(scaled_triangle, position_offset=(-400 + 2 * gap_x, 50))
turtle.color("purple")
write_label("Scaled Up (Rectangle)", (-400 + 2 * gap_x, -50))
draw_rectangle(scaled_rectangle, position_offset=(-400 + 2 * gap_x, -100))
turtle.hideturtle()
turtle.done()
