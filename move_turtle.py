import turtle

def move_forward():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def move_backward():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def move_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def move_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def reset_turtle():
    turtle.reset()

turtle.shape('turtle')

turtle.listen()
turtle.onkey(move_forward,"w")
turtle.onkey(move_backward,"s")
turtle.onkey(move_left,"a")
turtle.onkey(move_right,"d")
turtle.onkey(reset_turtle,"Escape")

turtle.mainloop()

    
    

