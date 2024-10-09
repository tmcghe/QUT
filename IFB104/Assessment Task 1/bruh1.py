import turtle

# Set up the turtle screen
turtle.setup(800, 600)

# Function to draw a rectangle at a given position with a given color
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to create a vertical gradient
def vertical_gradient(start_color, end_color, width, height):
    turtle.speed('fastest')  # Speed up the drawing

    # Calculate the gradient steps
    gradient_steps = 1000
    color_change = [(end_color[i] - start_color[i]) / gradient_steps for i in range(3)]

    # Draw each step of the gradient
    for step in range(gradient_steps):
        inter_color = [start_color[i] + step * color_change[i] for i in range(3)]
        color_tuple = tuple(inter_color)
        draw_rectangle(-width / 2, height / 2 - step * (height / gradient_steps),
                       width, height / gradient_steps, color_tuple)

    turtle.hideturtle()  # Hide the turtle

# Define the start and end colors as RGB tuples
start_color = (1, 0, 0)  # Red
end_color = (1, 0, 1)  # Yellow

# Create the gradient
vertical_gradient(start_color, end_color, 100, 100)

# Finish the drawing
turtle.done()