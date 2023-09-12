import turtle
def test_drive():
    turtle.forward (100)
    turtle.left (87)
    turtle.setheading (127)
    turtle.up()
    turtle.down()
    turtle.goto (50,50)
    turtle.home ()
    turtle.circle (69)
    
def turtle_state():
    print(turtle.isdown ())
    print(turtle.heading ())
    print(turtle.xcor(), turtle.ycor())

test_drive()
def main():
    test_drive()
    input ("press enter to continue")
    turtle_state()
main()