
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 12046230
student_name   = 'Thomas McGhee1'
#  NB: All files submitted for this assessable task will be subjected
#  to automated plagiarism analysis using a tool such as the Measure
#  of Software Similarity (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile
import math

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
config_file = 'assignment_1_config.py'
if isfile(config_file):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print(f"\nCannot find file '{config_file}', aborting!\n")
    abort()

# Define the function for generating data sets in Task 1B,
# using the imported raw data generation function if available,
# but otherwise creating a dummy function that just returns an
# empty list
data_file = 'assignment_1_data.py'
if isfile(data_file):
    print('Data generation module found ...\n')
    from assignment_1_data import raw_data
    def data_set(new_seed = randint(0, 99999)):
        return raw_data(new_seed) # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#

# All of your code goes in, or is called from, this function.
# In Task 1B ensure that your code does NOT call functions data_set
# or raw_data because they're already called in the main program
# below.
def visualise_data(rename_me_in_task_1b):

    def drip_but_never_drown(x,y,rot):
        ## used stackexchange, CS3621 mtu (and other mtu pages) and mainly Chatgpt to generate function "drip_but_never_drown" below, learning about basis functions why they are used in computing the biases for the convex hull etc, etc, I accept getting a 0. Rest was done purely by myself, i've done detailed notes on this function on paper as there is a lot of mathematics that i cant conceptualise into code but chatgpt was able to.
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

        def draw_gradient_water_drop(p0, p1, p2, p3, rotation_angle=0, rotation_center=(0, 0), color_start=(0, 0, 1), color_end=(1, 1, 1)):
            # Set the color mode to 255 (for RGB)
            colormode(255)
            width(2)
            
            penup()
            first_rotated_point = rotate_point(p0, rotation_angle, rotation_center)
            goto(first_rotated_point)
            
            # Create a list of points for the Bezier curve
            points = [rotate_point(cubic_bezier(p0, p1, p2, p3, t/100.0), rotation_angle, rotation_center) for t in range(101)]
            
            # Determine the height of the water drop for the gradient calculation
            min_y = min(points, key=lambda point: point[1])[1]
            max_y = max(points, key=lambda point: point[1])[1]
            height = max_y - min_y

            # Draw the gradient
            begin_fill()
            for point in points:
                color_t = (point[1] - min_y) / height
                r = int(color_start[0] * (1 - color_t) + color_end[0] * color_t)
                g = int(color_start[1] * (1 - color_t) + color_end[1] * color_t)
                b = int(color_start[2] * (1 - color_t) + color_end[2] * color_t)
                pencolor(r, g, b)
                goto(point)
                pendown()
            fillcolor((50, 50, 250))
            end_fill()

        def set_starting_position(x, y, p1_x, p1_y, p2_x, p2_y):
            p0 = (x, y)
            p1 = (p1_x, p1_y)
            p2 = (p2_x, p2_y)
            p3 = p0  # End at the start point to close the shape
            return p0, p1, p2, p3

        x_start, y_start = -x, y  # Absolute starting position
        p1_x, p1_y = x_start-(37.5), y_start-(18.75)  # relative points for bezier (first deriv)
        p2_x, p2_y = x_start+(3.75), y_start-(37.5)   # Second deriv point 

        # Setup the turtle speed and screen
        speed('fastest')
        hideturtle()  # Hide the turtle triangle for a cleaner look

        # Set the starting position and control points
        p0, p1, p2, p3 = set_starting_position(x_start, y_start, p1_x, p1_y, p2_x, p2_y)

        # Rotation parameters
        rotation_angle = math.radians(rot)  # Rotate by 45 degrees
        rotation_center = (p0[0], p0[1] - 50)  # Center of rotation, adjust if needed

        # Draw the water drop
        color_start = (0, 0, 255)  # Blue gradient start
        color_end = (255, 255, 255)  # White gradient end
        draw_gradient_water_drop(p0, p1, p2, p3, rotation_angle, rotation_center, color_start, color_end)


    logo1 = (-640,-100,-90)
    logo2 = (-640,400,90)
    def shape(x,y, rotation,txt1):
        #lt(rotation)
        pu()
        goto(x,y)
        pd()
        print('going to',int(x),int(y))
        speed('fast')
        #lt(90)
        fd(50)
        lt(90)
        fd(50)
        lt(180)
        begin_fill()
        width(5)
        color('black')
        for i in range(4):
            pd()
            fd(100)
            rt(90)
        fillcolor('red')
        end_fill()
        pu()
        rt(45)
        fd(70.71)
        pd()
        #lt(90)
        #fd(70.71)
        width(1)
        begin_fill()
        rt(45)
        fd(30)
        rt(90)
        color('black')
        fd(15)
        rt(90)
        fd(30)
        lt(135)
        fd(10)
        rt(180)
        circle(5,180)
        rt(180)
        fd(15)
        rt(45)
        fd(14)
        rt(90)
        circle(5,90)
        tracer(1,1)
        pu()
        speed('fastest')
        rt(90)
        fd(36)
        lt(90)
        pd()
        fd(15)
        lt(90)
        fd(30)
        rt(135)
        fd(9)

        lt(180)
        circle(-5,180)
        lt(180)
        fd(15)
        lt(45)
        fd(14)
        lt(90)
        circle(-5,90,360)
        fillcolor('blue')
        end_fill()
        #issues with rendering or rastering, increased steps to make it look better theoretically this code works but visually there is an issue
        #lt(45)
        #fd(70.71)
        #lt(90)
        #fd(70.71)
        pu()





    shape(*logo1, 'high')
    #issues with next part of assignment will arise with the water drop as its in absolutive values (of the canvas) instead of relative (to the logo)
    #below i used trial and error, did not calculate,set or initialise the relative rotation point to fit inside the logo nor did i set the logo rotation to correctly rotate relative to a fixed point as you can see by me inputting manual values in below, still learning.
    drip_but_never_drown(555,-128,0)
    shape(-540,50,180, 'mid')
    drip_but_never_drown(555,15,-90)
    shape(-540,100,180, 'low')
    drip_but_never_drown(555,227,-180)
    def salestext(x,y,txt1):
        print(f'Printing writeout for description of logo... Sales are {txt1}!')
        pu()
        goto(x,y)
        pd()
        color('black')
        write(f"Sales are {txt1}", font=("Arial",20))
    salestext(-655,60,'high')
    salestext(-655,-90,'mid')
    salestext(-655,-230,'low')
    
#
#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
#
# ***** You can add arguments to this function call to modify
# ***** features of the drawing canvas such as the background
# ***** and line colours, etc
create_drawing_canvas()

# Create the data set and pass it to the student's function
#
# ***** While developing your Task 1B code you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
#
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#
