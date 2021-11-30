from math import *
y1=1
deg=float(input("Enter the angle="))
g=9.81
u=float(input("Enter the intial velocity="))
x=float(input("Entet the value of x="))

rad=(pi/180)*deg
u=u/3.6
y = (x*tan(rad))+((g*(x**2))/(2*(u**2)*(cos(rad)**2)))
print("THE TRAJECTORY OF THE BALL IS, %.2f" % (y))
