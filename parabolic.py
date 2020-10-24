import math

#constants
g = -9.81

#projectile motion equations
def x_distance():
    return 0

#this will calc. z values for the parabola by taking the backwards order of the array given
def z(x):
    a = []
    for l in range(0,len(x)):
        a.append(0-(len(x)-l))
    return a
        
def X(init,final):
    p = []
    for i in range(init,final):
        p.append(i)
    return p

#generates a list from a quadratic equation
def parabolic(a,b,c,n):
    final = []
    for l in n:
        final.append(((-(a*(l))**2))+(b*l)+c)
    return final

def line(m,b,n):
    #y=mx+b
    final = []
    for l in range(0,n):
        final.append(m*(l)+b)
    return final

def trajectory(x,y,z):
    #x^2+0x+0
    return 0

#physics equations 
#x position
def finalX(angle,velocity):
    #l = math.pow(velocity,2)+2g(x[0]-x[1])
    a = (math.cos(math.radians(angle))*velocity)
    return 0