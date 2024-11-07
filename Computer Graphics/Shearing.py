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
def shear_shape(vertices, shear_factor_x, shear_factor_y):
    return [(x + shear_factor_x * y, y + shear_factor_y * x) for x, y in vertices]
turtle.speed(2)
turtle.bgcolor("white")
triangle_vertices = [(-100, 0), (0, 100), (100, 0)]
rectangle_vertices = [(-50, -50), (-50, 50), (50, 50), (50, -50)]
shear_factor_x = 0.5
shear_factor_y = 0.5
sheared_triangle = shear_shape(triangle_vertices, shear_factor_x, shear_factor_y)
sheared_rectangle = shear_shape(rectangle_vertices, shear_factor_x, shear_factor_y)
turtle.color("blue")
write_label("Original Triangle", (-400, 100))
draw_triangle(triangle_vertices, position_offset=(-400, 50))
turtle.color("green")
write_label("Original Rectangle", (-400, -50))
draw_rectangle(rectangle_vertices, position_offset=(-400, -100))
turtle.color("orange")
write_label("Sheared Triangle", (200, 100))
draw_triangle(sheared_triangle, position_offset=(200, 50))
turtle.color("brown")
write_label("Sheared Rectangle", (200, -70)) 
draw_rectangle(sheared_rectangle, position_offset=(200, -120)) 
turtle.hideturtle()
turtle.done()
