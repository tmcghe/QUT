
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
speed('fastest')
def visualise_data(dataset):
    title('house delivery')
    house()

    print(dataset)
    for data in dataset:
        print(data)
        print(data[0])
        print(data[1])

        month_coordinates = {
            'january':-400,
            'february':-320,
            'march':-240,
            'april':-160,
            'may':-80,
            'june':0,
            'july':80,
            'august':160,
            'september':240,
            'october':320,
            'november':400,
            'december':480
    }
        sales_y_coordinates ={
            -3:-280,
            -2:-200,
            -1:-120,
            0:-40,
            1:40,
            2:40,
            3:200,
    }

        #if x_coordinates is none:
            #continue
         # Draw each month coordinate
        for month, value in dataset:
        # Normalize month name to match keys in the dictionary
            x = month_coordinates.get(month.lower(), None)
            y = sales_y_coordinates.get(value, None)

            if x is not None and y is not None:
                data_house(x, y, f"{month.title()} ({value})")
            else:
                print(f"Warning: No coordinates available for {month} with value {value}")

def data_house(x,y,z):
    penup()
    goto (x,y)
    pendown()
    begin_fill()
    for _ in range(4):
        fillcolor("light green")
        forward(60) # length of the square sides
        right(90)   # turn 90 degrees to create corners
        pendown()
    end_fill()

       # Draw a square
    penup()
    goto(-560,160)
    pendown()
    begin_fill()
    for _ in range(4):

        fillcolor("blue")
        forward(25)  # Length of the square sides
        right(90)    # Turn 90 degrees to create corners
        pendown()
    end_fill()    
        
        # Move the turtle to the top left corner of the square
    penup()
        # Adjust the coordinates to position the triangle on top
    pendown()

        # Draw a triangle
    goto(-560,160)
    begin_fill()
    for _ in range(3):
        fillcolor("brown")
        forward(25)  # Length of the triangle sides
        left(120)     # Turn 120 degrees to create corners
        pendown()
    end_fill()    

        # move the turtle to the center of the triangle
    penup()
    goto(-547,163) # adjust the coordinates to position the circle
    pendown()

    penup()
    begin_fill()
        # draw a circle inside the triangle
    fillcolor("lightblue")
    circle(4)
    pendown()
    end_fill()

    penup()     
    goto(-590,100)
    write("sales are high", font=("arial",10))
    pendown()



    
    #draw a square
def house():
    penup()
    goto (-578,186)
    pendown()
    begin_fill()
    for _ in range(4):
        fillcolor("light green")
        forward(60) # length of the square sides
        right(90)   # turn 90 degrees to create corners
        pendown()
    end_fill()

       # Draw a square
    penup()
    goto(-560,160)
    pendown()
    begin_fill()
    for _ in range(4):

        fillcolor("blue")
        forward(25)  # Length of the square sides
        right(90)    # Turn 90 degrees to create corners
        pendown()
    end_fill()    
        
        # Move the turtle to the top left corner of the square
    penup()
        # Adjust the coordinates to position the triangle on top
    pendown()

        # Draw a triangle
    goto(-560,160)
    begin_fill()
    for _ in range(3):
        fillcolor("brown")
        forward(25)  # Length of the triangle sides
        left(120)     # Turn 120 degrees to create corners
        pendown()
    end_fill()    

        # move the turtle to the center of the triangle
    penup()
    goto(-547,163) # adjust the coordinates to position the circle
    pendown()

    penup()
    begin_fill()
        # draw a circle inside the triangle
    fillcolor("lightblue")
    circle(4)
    pendown()
    end_fill()

    penup()     #Australian productivity
    goto(-590,100)
    write("sales are high", font=("arial",10))
    pendown()


       #draw a square
    penup()
    goto (-578,20)
    pendown()
    begin_fill()
    for _ in range(4):
        fillcolor("yellow")
        forward(60) # length of the square sides
        right(90)   # turn 90 degrees to create corners
        pendown()
    end_fill()
                  
       # Draw a square
    penup()
    goto(-550,0)
    pendown()
    begin_fill()
    for _ in range(4):
        
        fillcolor("blue")
        forward(25)  # Length of the square sides
        right(90)     # Turn 90 degrees to create corners
        pendown()
    end_fill()

         # Move the turtle to the top left corner of the square
    penup()
    goto(-550,-25)     # Adjust the coordinates to position the triangle top
    pendown()

         # Draw a triangle
    left(90)    # to make the triangle face left
    begin_fill()
    for _ in range(3):
        fillcolor("brown")
        forward(25)  # Length of the triangle sides
        left(120)     # Turn 120 degrees to create corners
        pendown()
    end_fill()    

        # move the turtle to the center of the triangle
    penup()
    goto(-554,-12) # adjust the coordinates to position the circle
    pendown()

    penup()
    begin_fill()
        # draw a circle inside the triangle
    fillcolor("lightblue")
    circle(4)
    pendown()
    end_fill()

    
    penup()
    goto(-610,-70)
    write("sales are break even", font=("arial",10))
    pendown()


        #draw a square
    penup()
    goto (-578,-190)
    pendown()
    begin_fill()
    for _ in range(4):
        fillcolor("red")          
        forward(60) # length of the square sides
        right(90)   # turn 90 degrees to create corners
        pendown()
    end_fill()
     
        # Draw a square
    penup()
    goto(-560,-166)
    pendown()
    begin_fill()
    for _ in range(4):
        fillcolor("blue")
        forward(25)  # Length of the square sides
        right(90)     # Turn 90 degrees to create corners
        pendown()
    end_fill()    

        # Move the turtle to the left side of the square
    penup()
    goto(-535,-166) # Adjust the coordinates to position the triangle on
    pendown()

        # Draw a triangle
    left(90)   # to make the triangle face left
    begin_fill()
    for _ in range(3):
        fillcolor("brown")
        forward(25)  # Length of the triangle sides
        left(120)     # Turn 120 degrees to create corners
        pendown()
    end_fill()

        # move the turtle to the center of the triangle
    penup()
    goto(-547,-170) # adjust the coordinates to position the circle
    pendown()


    penup()
    begin_fill()
        # draw a circle inside the triangle
    fillcolor("lightblue")
    circle(4)
    pendown()
    end_fill()

    
    penup()
    goto(-590,-220)
    write("sales are low", font=("arial",10))
    pendown()




        
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
