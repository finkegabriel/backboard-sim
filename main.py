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

def paraBolEqn(data,a,b,c,d):
    x,y = data
    return -(((x-b)/a)**2+((y-d)/c)**2)+1.0
popt,pcov=optimize.curve_fit(paraBolEqn,np.vstack((doex,doey)),doez,p0=[1.5,0.4,1.5,0.4])

# x, y = np.meshgrid(np.linspace(np.min(doex), np.max(doex),1), np.linspace(np.min(doey),np.max(doey), 1))
# ax.plot_wireframe(x, y, paraBolEqn((x,y), *popt))

# bellow will draw points where the parabolic mesh should be top left, top right, center, bottom right, and bottom left points
ax.scatter(doex, doey, doez, color='b')
ax.scatter(doex[0],((doey[0]+doey[1])/2),((doez[0]+doez[2])/2),color='b')

xi = np.linspace(-5.5, 6.5, 500)
yi = .03*xi**2
yii = (((-xi*math.cos(theta)+yi*math.sin(theta)-h)**2)+k)

#plot of the top parabola to average with a matrix
ax.plot(yii+.4,-xi+((doey[0]+doey[1])/2),(doez[2]),zdir='z')

# second plot of the parabola off to the side of the hoop
xii = np.linspace(-5.5,6.5,500)
yii = .03*xii**2
yiii = (((-xi*math.cos(theta)+yi*math.sin(theta)-h)**2)+k)
ax.plot(yii+.4,xi+((doez[0]+doez[2])/2),((doey[0])),zdir='y')#(doey[0]),zdir='y')

# for x in range(len(xii)):
    #bottom right
print("x ",doex[0],doex[1],doex[2],doex[3])
    # ax.scatter(doex[0],doey[0],doez[0],color="green")
    #bottom left
print("y ",doey[0],doey[1],doey[2],doey[3])
    # ax.scatter(doex[1],doey[1],doez[1],color="green")
    #top left
print("z ",doez[0],doez[1],doez[2],doez[3])
    # ax.scatter(doex[2],doey[2],doez[2],color="green")
    #top right
# print("3 ",doex[3],doey[3],doez[3])
    # ax.scatter(doex[3],doey[3],doez[3],color="green")
    # A = [[doex[0],doey[0],doez[0]],
    #      [doex[1],doey[1],doez[1]],
    #      [doex[2],doey[2],doez[2]],
    #      [doex[3],doey[3],doez[3]]]
    # print(A)
    # xv,yv = np.meshgrid(xii,yii,indexing='ij')
    # print(xv,yv)
    # print(xv,yv)
    # for ix in range(xv):
    #     for iy in range(yv):
    #         print(ix,iy)
    # if x<=(len(xii)-2):
        # ax.scatter((xii[x]+xii[x+1])/2,(yii[x]+yii[x+1])/2,(doez[2]),zdir='y',color='blue')

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

for _ in range(0,1): #for loop to create multiple parabolas instances
    z = para.z(x,s,_)
    # ax.plot(x,s,'b--',zs=z,zdir="y")

g1.draw(ax,b,p,c)
plt.show()
importlib.reload(plt) 