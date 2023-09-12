import turtle
'''def test_drive():
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
main()'''
def square(a,b,c):
    turtle.pensize(4)
    turtle.pencolor("red")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(a)
        turtle.left(90)
    for i in range(4):
        turtle.forward(b)
        turtle.left(90)
    for i in range(4):
        turtle.forward(c)
        turtle.left(90)
    turtle.end_fill()
    turtle.bgcolor("pink")
    turtle.done()
    

a = int(input("enter the value:"))
b = int(input("enter the value:"))
c = int(input("enter the value:"))

square(a,b,c)
