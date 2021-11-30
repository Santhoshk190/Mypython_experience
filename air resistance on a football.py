m=float(input("Mass="))
g=9.81
fg=m*g
print("Force due to gravity",fg)
c=0.2
p=float(input("Air density rho="))
r=float(input("radius of ball="))
a=3.14*(r*r)
v=float(input("velocity="))
fd=0.5*p*a*(v**2)*c
print("Drag force-hard kick=",fd,"N")
#soft kick
v=float(input("velocity="))
a=3.14*(r**2)
fd=0.5*p*a*(v**2)*c
print("Drag force-soft kick=",fd,"N")

# take the values mentioned as below:
# Mass=0.43
#Force due to gravity 4.2183
#Air density rho=1.2
#radius of ball=0.11
#velocity=120
#Drag force-hard kick= 65.653632 N
#velocity=10
#Drag force-soft kick= 0.45592799999999994 N 
