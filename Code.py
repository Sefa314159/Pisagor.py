import math

def pisagor(x,y):
    if(x>100 or y>100):
        print ("Choose Leghts between (0,100)")
    else:
        c=math.sqrt((x**2)+(y**2))
        print ("First Lenght: {}\n".format(x))
        print ("Second Lenght: {}\n".format(y))
        print ("Hypotenuse: {}\n".format(c))
        print ("We have {} - {} - {} triangle".format(x, y, c))

while True:
    a=input("First Legth:")
    if (a == "q"):
        print ("Closing the app...")
        break
    a = float(a)
    if(a>100):
        print ("Choose Leght between (0,100)")
    else:
        b = input("Second Lenght:")
        if (b == "q"):
            print("Closing the app...")
            break
        b = float(b)
        if (b > 100):
            print ("Choose Leght between (0,100)")
        else:
            pisagor(a,b)
