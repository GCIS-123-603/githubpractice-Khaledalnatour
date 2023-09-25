#Importing Turtle
import turtle as t
#importing random integer from random module
from random import randint
#background color
t.bgcolor ("pale turquoise")
#function for star
def star():
    t.pencolor("white")
    t.fillcolor("black")
    t.begin_fill()
    for i in range (5):
        t.forward(20)
        t.right(144)
    t.end_fill()
#Multiple stars using randomint module
def mstars():
    for i in range (25):
        x= randint(-400,400)
        y= randint(-250,250)
        star()
        t.up()
        t.goto(x,y)
        t.down()



#Function for drawing a table
def table():
    t.up()
    t.goto(0,-10)
    i=0
    while i < 2:

        i = 0
        length = int(input("Table length: "))

        if length > 1000:
            print("Please enter a lower value")
        elif length < 500:
            print("Please enter higher value")
        else:
            i += 1

        if length%100 != 0:
            print("Please enter number divisible by 100")
        else:
            i += 1

    i = 0
    while i < 1:

        i = 0
        height = int(input("Enter leg height: "))

        if height > 400:
            print("Please enter a lower value")
        elif height < 100:
            print("Please enter higher value")
        else:
            i += 1

    t.down()
    t.fillcolor("chocolate")
    t.begin_fill()
    t.forward(length/2)
    t.right(90)
    t.forward(0.05*length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(0.05*length)
    t.right(90)
    t.forward(length/2)
    t.end_fill()
    t.up()
    t.right(90)
    t.forward(0.05*length)
    t.left(90)
    t.forward(length/2)
    t.right(180)
    t.down()
    t.forward(0.1*length)
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(0.05*length)
    t.right(90)
    t.forward(height)
    t.end_fill()
    t.left(90)
    t.forward(0.05*length)
    t.begin_fill()
    t.left(90)
    t.forward(height-50)
    t.right(90)
    t.forward(0.05*length)
    t.right(90)
    t.forward(height - 50)
    t.end_fill()
    t.left(90)
    t.forward(0.5*length)
    t.begin_fill()
    t.left(90)
    t.forward(height - 50)
    t.right(90)
    t.forward(0.05*length)
    t.right(90)
    t.forward(height-50)
    t.end_fill()
    t.left(90)
    t.forward(0.05*length)
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(0.05*length)
    t.right(90)
    t.forward(height)
    t.end_fill()
    t.up()
    t.goto(0,0)


#Function for drawing the plate
def plate():
    plate_lenght = 300
    t.goto(0,0)
    t.right(90)
    t.fillcolor("white")
    t.begin_fill()
    t.forward(plate_lenght/2)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(plate_lenght)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(plate_lenght/2)
    t.end_fill()


#Function for drawing first layer of cake
def cake1 (a,clr,):
    t.down()
    t.pensize (4)
    t.pencolor ("brown")
    t.fillcolor (clr)
    t.begin_fill ()
    for i in range (2):
        t.forward (a)
        t.left (90)
        t.forward(a/2)
        t.left(90)
        t.forward (a)
    t.end_fill()

        
    t.up()
    t.forward (a/2)
    t.left(90)
    t.forward(a/2)
    t.left(90)
    t.forward (a/2)
    
#Function for drawing second layer of cake  
def cake2 (a,clr2):
    t.pensize (4)
    t.pencolor ("brown")
    t.fillcolor (clr2)
    t.begin_fill ()
    for i in range (2):
        t.down()
        b =  a -10
        t. forward (b)
        t.right (90)
        t.forward(b/2)
        t.right(90)
        t.forward(b)
        
    t.up()
    t.right(90)
    t.forward(b/2)
    t.left(90)
    t.end_fill()

#Function for drawing first layer of cake
def cake3(a,clr3):
    t.pensize(4)
    t.pencolor ("brown")
    t.fillcolor (clr3)
    t.begin_fill ()
    for i in range (2):
        c = a - 20
        t.down()
        t.forward (c)
        t.right(90)
        t.forward (c/2)
        t.right(90)
        t.forward (c)
    t.up()
    t.right(90)
    t.forward(c/2)
    t.left(90)
    t.end_fill()

#Function for drawing Star Icing
def icing(a,iceclr):
    t.setheading(270)
    t.up()
    t.forward(a/10)
    t.pencolor("white")
    t.fillcolor(iceclr)
    t.begin_fill()
    for i in range (5):
        t.forward(a/5)
        t.right(144)
    t.end_fill()
    t.setheading(90)
    t.up()
    t.forward(a/10)
    t.setheading(180)

#Function for drawing Candle on Cake
def candle(a):
    t.pensize (4)
    t.pencolor ("brown")
    t.fillcolor ("coral")
    t.begin_fill()
    for i in range (2):
        t.down()
        t.forward (a/10)
        t.right (90)
        t.forward(a/2)
        t.right(90)
        t.forward(a/10)
    t.end_fill()
    t.fillcolor ("yellow")
    t.back(a/10)
    t.right(90)
    t.up()
    t.forward(a/1.5)
    t.down()
    t.pensize (1)
    t.begin_fill()
    t.circle(a/10)
    t.end_fill()

#Function for saying Happy Birthday

def bdaysign():
    t.up()
    t.color('red')
    t.goto(0,290)
    style=("courier" , 30,"italic bold")
    t.down()
    t.write('Happy Birthday!', font=style, align='center')

#Function for Writing authors names
def authors():
    t.up()
    t.color('red')
    t.goto(280,-310)
    style=("courier" , 10,"italic")
    t.down()
    t.write('Khalid, Lohith, Zahid', font=style, align='center')
    t.up()
   

#Writing DocStrings
def docstr1():
    '''Today, you will be drawing a cake using turtle on python.
    You will be inputing the data as asked by the program.'''
    return None


def docstr2():
    '''(0-100) (Enter 100 for the perfect size)'''
    return None

def docstr3():
    '''Enter 500 as table lenght and 250 for legs for perfect size'''
    return None

def docstr4():
    '''Thank you for taking part, hope you enjoyed it.'''
    return None



    
#Calling all functions
 
def main():
    print(docstr1.__doc__)
    t.speed(0)
    mstars()
    t.speed(5)
    print(docstr2.__doc__)
    a = int (input("Enter the size of first cake layer: "))
    print(docstr3.__doc__)
    table()
    print(docstr4.__doc__)
    plate()       
    clr = str (input("Enter the color of the first cake layer:\n"))
    clr2 = str (input("enter the color of the second cake layer: \n"))
    clr3 = str (input("enter the color of the third cake layer:\n"))
    iceclr= str (input("enter the color of the star icing:\n"))
    cake1 (a, clr)
    cake2 (a,clr2)
    cake3 (a,clr3)
    icing(a,iceclr)
    candle(a)
    bdaysign()
    authors()
    t.home()
    print(docstr4.__doc__)
    a = input("Press enter to terminate")



#Calling main function
main()

#End of program
