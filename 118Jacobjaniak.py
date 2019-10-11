import turtle as trtl


trees_turtle = trtl.Turtle()
bike_turtle = trtl.Turtle()
environment_turtle = trtl.Turtle()
ground_turtle = trtl.Turtle()

#code for the ground of where the objects will lay on
ground_turtle.goto(0,0)
ground_turtle.forward(500)
ground_turtle.penup()
ground_turtle.goto(0,0)
ground_turtle.right(180)
ground_turtle.pendown()
ground_turtle.forward(500)

#code for environment 
environment_turtle.penup()
environment_turtle.goto(-380,0)
environment_turtle.pendown()
environment_turtle.circle(20)
environment_turtle.penup()
environment_turtle.goto(390,0)
environment_turtle.pendown()
environment_turtle.circle(25)
environment_turtle.penup()
environment_turtle.goto(-450,0)
environment_turtle.pendown()
environment_turtle.right(270)
environment_turtle.forward(50)
environment_turtle.penup()
environment_turtle.goto(-450,0)
environment_turtle.pendown()
environment_turtle.circle(70,50)
environment_turtle.penup()
environment_turtle.goto(-450,0)
environment_turtle.pendown()
environment_turtle.circle(70,50)
environment_turtle.penup()
environment_turtle.goto(-450,0)
environment_turtle.pendown()
environment_turtle.right(180)
environment_turtle.circle(50,70)
environment_turtle.penup()
environment_turtle.goto(-450,0)
environment_turtle.pendown()
environment_turtle.circle(70,60)
environment_turtle.penup()
environment_turtle.goto(450,0)
environment_turtle.pendown()
environment_turtle.circle(70,50)
environment_turtle.penup()
environment_turtle.goto(450,0)
environment_turtle.pendown()
environment_turtle.circle(70,50)
environment_turtle.penup()
environment_turtle.goto(450,0)
environment_turtle.pendown()
environment_turtle.right(180)
environment_turtle.circle(50,70)
environment_turtle.penup()
environment_turtle.goto(450,0)
environment_turtle.pendown()
environment_turtle.circle(70,60)
environment_turtle.penup()
environment_turtle.goto(450,0)
environment_turtle.pendown()








#code for trees
trees_turtle.penup()
trees_turtle.goto(-240,0)
trees_turtle.pendown()
trees_turtle.circle(30,90)
trees_turtle.forward(250)
trees_turtle.circle(-55,340)






wn = trtl.Screen()
wn.mainloop()