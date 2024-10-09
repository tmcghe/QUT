import math
from turtle import Screen, Turtle

def cubic_bezier(p0, p1, p2, p3, t):
    """Calculate a point on a cubic Bezier curve given four control points and parameter t."""
    x = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t) * t**2 * p2[0] + t**3 * p3[0]
    y = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t) * t**2 * p2[1] + t**3 * p3[1]
    return (x, y)

def rotate_point(point, angle, center):
    """Rotate a point around a center by a given angle."""
    ox, oy = center
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def draw_water_drop(turtle, p0, p1, p2, p3, rotation_angle=0, rotation_center=(0, 0)):
    """Draw a water drop shape using a cubic Bezier curve with rotation."""
    turtle.penup()
    turtle.goto(p0)
    turtle.pendown()
    
    for t in range(101):
        point = cubic_bezier(p0, p1, p2, p3, t/100.0)
        rotated_point = rotate_point(point, rotation_angle, rotation_center)
        turtle.goto(rotated_point)

def set_starting_position(x, y, p1_x, p1_y, p2_x, p2_y):
    """Set starting position and control points using absolute coordinates."""
    p0 = (x, y)
    p1 = (p1_x, p1_y)
    p2 = (p2_x, p2_y)
    p3 = p0  # End at the start point to close the shape
    
    return p0, p1, p2, p3

# Example of setting absolute positions

x_start, y_start = -150, 20  # Absolute starting position
p1_x, p1_y = x_start-50, y_start-25  # First control point
p2_x, p2_y = x_start+5, y_start-50   # Second control point

screen = Screen()
turtle = Turtle()
turtle.speed('fastest')

p0, p1, p2, p3 = set_starting_position(x_start, y_start, p1_x, p1_y, p2_x, p2_y)

# Print initial position
print(f"Initial position: {p0}")

# Rotation parameters
rotation_angle = math.radians(120)  # Rotate by 45 degrees
rotation_center = (p0[0], p0[1] - 50)  # Center of rotation, adjust if needed

draw_water_drop(turtle, p0, p1, p2, p3, rotation_angle, rotation_center)

