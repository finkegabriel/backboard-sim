import math

#constants
g = -9.81

#projectile motion equations
def x_distance():
    return 0

#this will calc. z values for the parabola by taking the backwards order of the array given
#TODO needs an offset range so it does not miss the backboard 
def z(x):
    a = []
    for l in range(0,len(x)):
        a.append(0-(x[l]))
    return a

#we are rotating counter clock wise
def rotate(x,y,rot):
    # print(x,"\n",y)
    finalx = []
    finaly = []
    for l in range(len(x)):
        xf = [1+math.floor(math.cos(rot)),0-1-math.floor(math.sin(rot))]
        yf = [1-math.floor(math.sin(rot)),1+math.floor(math.cos(rot))]
        # print(
        # "xf ",xf," x ",x," \n",
        # "yf ",yf," y ",y," \n")
        finalx.append((xf[0]*x[l])+(xf[1]*y[l]))
        finaly.append((yf[0]*x[l])+(yf[1]*y[l]))
        # print(l)
        # print("xf ",finalx," ",len(finalx)," \n",
        #       "yf ",finaly," ",len(finaly)," \n")
    return finalx,finaly

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