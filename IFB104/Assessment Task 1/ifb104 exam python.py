from turtle import *



#making the dimensions look similar to that of the screenshot
exampg = Screen()

exampg.setup(500,500)
#making it look like its in the center like the program image is
pu()
goto(100,100)
setheading(90)
pd()

### using the circle command to draw the circle, a loop could also suffice
color('blue')
fillcolor('red')
begin_fill()
width('10')
speed('fastest')
#below draws circle 200 in diameter, 360 steps or loops for the full rotation, and an extent value thats left the same as implied default
circle(100,extent = 360,steps = 360)
end_fill()
#face towards origin of circle
lt(90)
#draws triangle
fillcolor('yellow')
begin_fill()
for i in range(3):
	fd(200)
	lt(120)

end_fill()
#lets you see the final product
done()