import math

#constants
g = -9.81

#projectile motion equations
def x_distance():
    return 0

def betterZ(x,y,offset):
    print("z")
    final = []
    # z = ((offset/y)*((x-x)**2)+y)    
    return final

#this will calc. z values
#TODO needs an offset range so it does not miss the backboard 
def z(x,y,zval):
    z = []
    for l in range(len(x)):
        #z0 = x[l]**2+y[l]**2
        z0 = l-zval
        z.append(z0)
    return z

#we are rotating counter clock wise
def rotate(x,y,rot):
    # print(x,"\n",y)
    z = []
    for l in range(len(x)):
        xf = [(math.cos(math.radians(rot))),(math.sin(math.radians(rot)))]
        yf = [(math.sin(math.radians(rot))),(math.cos(math.radians(rot)))]
        # print(
        # "xf ",xf," x ",x[l]," \n",
        # "yf ",yf," y ",y[l]," \n")
        z.append((yf[0]*x[l])+(yf[1]*y[l]))
        # finalx.append((xf[0]*x[l])-(yf[1]*y[l]))
        # finaly.append((yf[0]*x[l])+(yf[1]*y[l]))
        # print("xf ",finalx," "," \n",
        #       "yf ",finaly," "," \n")
    return z

def X(init,final):
    p = []
    for i in range(init,final):
        p.append(i)
    return p

#this function will compute a parabola and its vertex rotated on its side
# y = -b/2a
# x = 
def parabolic(a,b,c,n):
    finaly = []
    for x in n:
        # final.append()
        finaly.append(((-(a*(x))**2))+(b*x)+c)
    #print(finaly)
    return finaly

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
