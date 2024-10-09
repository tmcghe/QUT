
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
    print('hi')


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
def visualise_data(dataset):

    print('here is the dataset'+str(dataset))
    '''
    if (dataset[1] == 0):
        pd()
        color('yellow')
    elif(dataset[1] > 0): #if its above 1
        pd()
        color('green')
        value = dataset[1] 
        if (value > 3):
            value = 3
        for i in range(data[1]+1):
            print(i)
'''

    #print(str(raw_data(new_seed)+'hello'))


    #print(str(raw_data(new_seed)+'hello'))

    def drip_but_never_drown(x,y,rot):
        #function is never called, this isnt apart of the assessment and it doesn't complete the assignment the 'right way' so not bothering with it.
        
        
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
        #speed('fastest')
        tracer(0)
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


    logo1 = (-640,-100,0)
    logo2 = (-640,400,0)
    
    def shape(x,y, rotation,txt1):
        import time
       # time.sleep(2)
        #write(str(pos()))
        fix_rot = [['low', -60,60],['mid',-60,0],['high',0,0]]
        for i in range(len(fix_rot)): #solves the issue of having the coordinates start differently, i cant code rotation matrixes yet like above (which is what chatgpt did source: https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python), so simple vector translation will suffice.
            #print(fix_rot[i][0])
            if fix_rot[i][0] == txt1:
                print(fix_rot[i][1], fix_rot[i][2])
                x -= fix_rot[i][1]
                y -= fix_rot[i][2]


        lt(rotation)
        pu()
        goto(x,y)
        #write(str(pos()))
        pd()
        print('going to',int(x),int(y))
        #write(str(pos()))
        tracer(0)
        begin_fill()
        width(1)
        color('black')
        for i in range(4):
            pd()
            fd(60)
            rt(90)
            #write(str(pos()))
            #print(str(pos()))
        if txt1 == 'low':
            fillcolor('red')
        if txt1 == 'mid':
            fillcolor('orange')
        if txt1 == 'high':
            fillcolor('green')
        end_fill()
        pu()
        rt(45)
        fd(41.141)
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
        #tracer(0)
        pu()
        #speed('fastest')
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
        setheading(0)




    
    '''shape(-640,-100,0, 'high')'''
    '''
    #issues with next part of assignment will arise with the water drop as its in absolutive values (of the canvas) instead of relative (to the logo)
    #below i used trial and error, did not calculate,set or initialise the relative rotation point to fit inside the logo nor did i set the logo rotation to correctly rotate relative to a fixed point as you can see by me inputting manual values in below, still learning.
    drip_but_never_drown(555,-128,50)
    shape(-540,50,-90, 'mid')
    drip_but_never_drown(618,15,-40)
    shape(-540,100,180, 'low')
    drip_but_never_drown(625,227,-130)
    '''
    shape(-630,160,0, 'high')
    shape(-630,30,-90, 'mid')
    shape(-630,-100,180, 'low')
    #shape(-360,100,0, 'high')
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
    print(dataset)

    xvals = {
        "January":-300,
        "February":-240,
        "March":-180,
        "April":-120,
        "May":-60,
        "June":0,
        "July":60,
        "August":120,
        "September":180,
        "October":240,
        "November":300,
        "December":360

    }

    yvals = {
        -3:-150,
        -2:-90,
        -1:-30,
        0:30,
        1:90,
        2:150,
        3:210



    }
    for dnum in range(len(dataset)):
        try:
            value = dataset[dnum][1]
            month = dataset[dnum][0]
            xval = xvals.get(month)
            if value > 3:
                yval = yvals[3]
            elif value < -3:
                yval = yvals[-3]
            else:
                yval = yvals.get(value)
            #xval = 0
            print('the month is ' + str(month))
            print('and our position is: ' + str(value))
            print('therefore our x and y values are: {},{}'.format(xval, yval))

            if value > 0:
                print('we are above positive')
                goto(xval, yval)  # Correct usage of goto
                #write(xval,yval)
                #write('pos')
                #shape(xval,yval,1,'high')
                for i in range(abs(value)+1):
                    if i > 3:
                        break
                    else:
                        #print('###############LOOP IS RUNNING####')
                        yval = yvals.get(i)
                        shape(xval,yval,0,'high')
            elif value == 0:
                print('we are neutral')
                goto(xval, yval)
                #write(xval,yval)
                #write('neutral')  # Go to the coordinate and maybe do something like drawing a dot
                #dot(5)  # Drawing a dot at the location
                shape(xval,yval,-90,'mid')
            elif value < 0:
                print('we are negative')
                goto(xval, 0)
                #write(xval,0)
                #write('neg')
                dot(5)  # Drawing a dot at the location
                for i in range(abs(value)+1):
                    if i > 3:
                        break
                    else:
                        #print('###############LOOP IS RUNNING####')
                        yval = (yvals.get(i)*-1)+60
                        shape(xval,yval,-180,'low')
        except Exception as e:
            print(f"Oops, report didn't come through! handling exception: {e}")
            continue  # Skip to the next iteration of the loop if report wasn't inside the data

        
        money = 0         
    for i in range(len(dataset)):
        print(money)
        #print('1')
        value = dataset[i][1]
        print(value)
        money += value
        #print(money)
    print('###MONEY IS'+str(money))
    goto(-400,-400)
    write('Net Profit: $'+str(money),font=("Arial", 40, "normal"))



        
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
create_drawing_canvas('Clothing Industry, data processing')

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
