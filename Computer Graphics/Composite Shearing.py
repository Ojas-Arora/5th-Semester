import turtle

def write_label(label, position):
    turtle.penup()
    turtle.goto(position[0], position[1] + 20)  
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

def draw_points(vertices, position_offset=(0, 0), color="black"):
    turtle.color(color)
    for x, y in vertices:
        turtle.penup()
        turtle.goto(x + position_offset[0], y + position_offset[1])
        turtle.pendown()
        turtle.dot(5)
        turtle.penup()
        turtle.goto(x + position_offset[0] + 10, y + position_offset[1])
        turtle.pendown()
        turtle.write(f"({x}, {y})", align="left", font=("Arial", 10, "normal"))

def shear_shape_composite(vertices, shear_factor_x, shear_factor_y, shear_origin):
    translated_vertices = [(x - shear_origin[0], y - shear_origin[1]) for x, y in vertices]
    sheared_vertices = [(x + shear_factor_x * y, y + shear_factor_y * x) for x, y in translated_vertices]
    final_vertices = [(x + shear_origin[0], y + shear_origin[1]) for x, y in sheared_vertices]
    return final_vertices

turtle.speed(2)
turtle.bgcolor("white")

triangle_vertices = [(-100, 0), (0, 100), (100, 0)]
rectangle_vertices = [(-50, -50), (-50, 50), (50, 50), (50, -50)]

shear_factor_x = 0.5
shear_factor_y = 0.5

shear_origin_triangle = (50, 50)
shear_origin_rectangle = (50, 50)

sheared_triangle = shear_shape_composite(triangle_vertices, shear_factor_x, shear_factor_y, shear_origin_triangle)
sheared_rectangle = shear_shape_composite(rectangle_vertices, shear_factor_x, shear_factor_y, shear_origin_rectangle)

turtle.color("blue")
write_label("Original Triangle", (-400, 150))
draw_shape(triangle_vertices, position_offset=(-400, 50))
draw_points(triangle_vertices, position_offset=(-400, 50), color="blue")

turtle.color("green")
write_label("Original Rectangle", (-400, -50))
draw_shape(rectangle_vertices, position_offset=(-400, -100))
draw_points(rectangle_vertices, position_offset=(-400, -100), color="green")

turtle.color("orange")
write_label("Sheared Triangle (Composite)", (200, 150))
draw_shape(sheared_triangle, position_offset=(200, 50))
draw_points(sheared_triangle, position_offset=(200, 50), color="orange")

turtle.color("brown")
write_label("Sheared Rectangle (Composite)", (200, -70)) 
draw_shape(sheared_rectangle, position_offset=(200, -120))
draw_points(sheared_rectangle, position_offset=(200, -120), color="brown")

turtle.hideturtle()
turtle.done()
