import time
import math
import matplotlib.pyplot as plt
try:
 choice=int(input("""Please select:
1.Simple calculation
2.Advance calculation
3.Graph plotting
"""))
 match choice:
    case 1:
           x=float(input("Please enter the number 1:"))
           z=int(input("""Please select  
           1.Addition
           2.Subtraction
           3.Multiplication
           4.Division(quotient)
           5.Division(remainder)
           """))
           y=float(input("Please enter the number 2:"))
           match(z):
                    case 1:
                           s=x+y
                           print("Sum=",s)
                    case 2:
                           d=x-y
                           print("Difference=",d)
                    case 3:
                           p=x*y
                           print("Product=",p)
                    case 4:
                           q=x/y
                           print("Quotient=",q)
                    case 5:
                           r=x%y
                           print("Remainder=",r)
                    case _:
                           print("Invalid input")
    case 2:
           x1=float(input("Please enter the number 1:"))
           z1=int(input("""Please select:
           1.Squaring the number
           2.Cubing the number
           3.Mod of the number
           4.Inverse of the number
           5.Square root of the number
           6.Cube root of a number
           7.Ceiling value of the number
           8.Floor value of the number
           9.Check whether the number is prime or not
           10.Convert degree to radians
           11.Convert radians to degree
           12.Sine value
           13.Cosine value
           14.Tangent Value
           15.Cotangent Value
           16.Secent value
           17.Cosecent value"""))
           match z1:
                    case 1:
                           y1=x1*x1
                           print(f"Square of {x1}=", y1)
                    case 2:
                          y1=x1*x1*x1
                          print(f"Cube of {x1}=",y1)
                    case 3:
                          y1=math.abs(x1)
                          print(f"Mod of {x1}=", y1)
                    case 4:
                           y1=float(1/x1)
                           print(f"Inverse of {x1}=", y1)
                    case 5:
                           y1=math.sqrt(x1)
                           print(f"Square-root of {x1}=", y1)
                    case 6:
                           y1=math.cbrt(x1)
                           print(f"Cube-root of {x1}=",y1)
                    case 7:
                           y1=math.ceil(x1)
                           print(f"Ceiling value of {x1}=",y1)
                    case 8:
                           y1=math.floor(x1)
                           print(f"Floor value of {x1}=", y1)
                    case 9:
                        x1=int(x1)
                        q=0
                        for i in range(2,x1):
                            if(x1%i==0):
                                q+=1
                        if(q>0):
                            print("Number is not prime")
                        else:
                            print("Number is prime")
                    case 10:
                            y1=math.radians(x1)
                            print(f"The radian value of {x1}=",y1)
                    case 11:
                            y1=math.degrees(x1)
                            print(f"The degree value of {x1}=", y1)
                    case 12:
                            y1=math.sin(x1)
                            print(f"The sine value of {x1}=",y1)
                    case 13:
                            y1=math.cos(x1)
                            print(f"The cosine value of {x1}=",y1)
                    case 14:
                            y1=math.tan(x1)
                            print(f"The tangent value of {x1}=",y1)
                    case 15:
                            y1=math.cot(x1)
                            print(f"The cotangent value of {x1}=",y1)
                    case 16:
                            y1=math.sec(x1)
                            print(f"The secant value of {x1}=",y1)
                    case 17:
                            y1=math.cosec(x1)
                            print(f"The cosecant value of {x1}=",y1)
                    case _:
                          print("Invalid input")
    case 3:
        xlist = []
        ylist = []
        inn = int(input("Please enter the number of points you want to plot"))
        title = str(input("Please enter the title of the graph"))
        xaxis=str(input("Please enter the Xlabel"))
        yaxis=str(input("Please enter the Ylabel"))
        for i in range(0, inn):
            x = float(input("Please enter the X coordinates"))
            y = float(input("Please enter the Y coordinates"))
            xlist.insert(i, x)
            ylist.insert(i, y)
        print(xlist)
        plt.plot(xlist, ylist)
        plt.xlabel(xaxis)
        plt.ylabel(yaxis)
        plt.title(title)
        plt.show()
    case _:
         print("Invalid input")
except:
    print("Please enter valid value!")
else:
 time=time.strftime("%H:%M")
 print(time)