import turtle

def draw_shirt():
    turtle.speed('slow')  # Set drawing speed
    
    # Start drawing the body of the shirt
    turtle.color('blue')
    turtle.begin_fill()
    turtle.forward(100)  # Bottom edge
    turtle.left(90)
    turtle.forward(150)  # Right side
    turtle.right(45)
    turtle.forward(30)  # Right sleeve
    turtle.right(90)
    turtle.forward(30)  # Right sleeve top
    turtle.right(90)
    turtle.forward(30)  # Right sleeve back
    turtle.left(45)
    turtle.forward(150)  # Top edge
    turtle.left(45)
    turtle.forward(30)  # Left sleeve
    turtle.left(90)
    turtle.forward(30)  # Left sleeve top
    turtle.left(90)
    turtle.forward(30)  # Left sleeve back
    turtle.end_fill()
    
    # Draw the collar
    turtle.color('white')
    turtle.goto(50, 150)  # Position at the middle top of the shirt
    turtle.begin_fill()
    turtle.circle(20)  # Simple round collar
    turtle.end_fill()

    turtle.hideturtle()  # Hide turtle after drawing is complete

# Set up the screen
turtle.setup(400, 400)
turtle.title("Turtle Shirt")

draw_shirt()

# Keep the window open until it's closed by the user
turtle.done()
