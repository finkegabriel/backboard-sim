from turtle import color
from matplotlib.patches import Rectangle,Circle
from translate import Translate
from graph import Graph
import matplotlib.pyplot as plt
import numpy as np
import parabolic as para
import importlib
from datetime import datetime, timedelta
import scipy.optimize as optimize
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R
import math as math
import scipy.optimize as opt
import motion as motion

t1 = Translate()
g1 = Graph()
ax = plt.axes(projection="3d")

doex = [.4,.4,.4,.4]
doey = [11,2,2,11]
doez = [9.9,9.9,15.9,15.9]

#draw a paraobola along the x,z (side view) axis 
#draw a parabola along the y,z (front view) axis
#(ax^2+bx+c)
#x=(-b/2a)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
theta = 1.52
h= 0
k= 0

xParaBounds = 9
yParaBounds = 7

# bellow will draw points where the parabolic mesh should be top left, top right, center, bottom right, and bottom left points
ax.scatter(doex, doey, doez, color='b')
ax.scatter(doex[0],((doey[0]+doey[1])/2),((doez[0]+doez[2])/2),color='b')

xi = np.linspace(-5.5, 6.5, 500)
yi = .03*xi**2
yii = (((-xi*math.cos(theta)+yi*math.sin(theta)-h)**2)+k)

#plot of the top parabola to average with a matrix
ax.plot(yii+.4,-xi+((doey[0]+doey[1])/2),(doez[2]),zdir='z',color='green')

# second plot of the parabola off to the side of the hoop
xii = np.linspace(-5.5,6.5,500)
yii = .03*xii**2
yiii = (((-xi*math.cos(theta)+yi*math.sin(theta)-h)**2)+k)
ax.plot(yii+.4,xi+((doez[0]+doez[2])/2),((doey[0])),zdir='y',color='green')#(doey[0]),zdir='y')

xiii = np.linspace(-5.5,6.5,500)
yiiii = .03*xii**2
yiiiii = (((-xi*math.cos(theta)+yi*math.sin(theta)-h)**2)+k)

########
xip = np.linspace(0, 10, 500)
yip = .09*-xip**2+12
ax.plot(xip,yip,10,zdir='y',color='black')
########

for oX in range(xParaBounds):
    ax.plot(yiiii+.4,xiii+((doez[0]+doez[2])/2),((doey[1])+oX),zdir='y',color='green')

for oY in range(yParaBounds):
    ax.plot(yi+.4,-xi+((doey[0]+doey[1])/2),(doez[2]-oY),zdir='z',color='green')

motion.trackBoundry()
guess = (1,1)
#draw hoop, arrays are for x, y location on the graph
backboard=[5,11.5]
xy=[2,10]
#hoop location parameters
circlexy=[2.25,6.5]
x = para.X(0,15)
s = para.parabolic(.3,0,12,x)

b = Rectangle(backboard,3,2.25,fill=False,color='red')
c = Circle((circlexy),radius=2.25,fill=False)
#72 - 9 48 - 6 
p = Rectangle(xy,9,6,edgecolor='red',facecolor='none')

# for _ in range(0,1): #for loop to create multiple parabolas instances
#     z = para.z(x,s,_)
    # ax.plot(x,s,'b--',zs=z,zdir="y")

g1.draw(ax,b,p,c)
plt.show()
importlib.reload(plt) 
