def add (x,y):
    return x + y


def minus (x,y):
    return x - y
    

def multiply (x,y):
    return x * y


def divide (x,y):
    return  x / y

def main():
    x = int(input("enter the first value: "))
    y = int(input("enter the second value:"))
    print ("when you add both these values you get: ", add(x,y) )
    print ("when you minus both these values you get: ", minus(x,y) )
    print ("when you multiply both these values you get: ", multiply(x,y) )
    print ("when you divide both these values you get:", divide(x,y) )
main()