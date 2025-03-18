import turtle as t # importing turtle

#function for half circle
def loop():
    for i in range(100):
        t.fd(2) 
        t.lt(2)

#main code      
t.speed(0)#speed
t.title("THE RED HEART")#title
t.bgcolor('pink')#backgroud colour
t.pensize(10)#size of the pen
t.color('red')#colour of the heart
t.begin_fill()# start coloring
t.lt(45)
t.fd(110)
loop()
t.rt(120)
loop()
t.fd(115)
t.end_fill()# end coloring

#arrow
t.rt(50+90)
t.penup()
t.fd(100)
t.pendown()
t.rt(50+90)
t.pensize(20)
t.shapesize(5)
t.shape("arrow")
t.fd(300)

# Create a turtle object
T= t.Turtle()

# Move the turtle to position
T.penup()
T.goto(-50, -500)
T.pendown()

T.color("red")
T.begin_fill()
# Write the sentence
T.write("I love You", font=("Arial", 30, "bold"), align="center")
T.end_fill()

# Hide the turtle and finish
T.hideturtle()

# for screen running
t.mainloop()