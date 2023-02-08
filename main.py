from matplotlib.patches import Rectangle,Circle
from graph import Graph
import matplotlib.pyplot as plt
import numpy as np
import importlib
from datetime import datetime, timedelta
import scipy.optimize as optimize
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R
import math as math
import csvfile as csvTool
import random as random

g1 = Graph()
ax = plt.axes(projection="3d")

def player(theta,vel):
    print(theta,vel)

def random_time(x,y,z):
    doex = [.4,.4,.4,.4]
    doey = [11,2,2,11]
    doez = [9.9,9.9,15.9,15.9]
    
    maxX = max(doex)
    maxY = max(doey)
    maxZ = max(doez)

    minX = min(doex)
    minY = min(doey)
    minZ = min(doez)+.5

    randX = random.uniform(minX,maxX)
    randY = random.uniform(minY,maxY)
    randZ = random.uniform(minZ,maxZ)
    x4,y4,z4 = [randX,x],[randY,y],[randZ,z]

    ax.scatter(randX,randY,randZ,zdir='z',color='purple')
    ax.plot(x4,y4,z4,zdir='z',linestyle='--',color='purple')
    return {"x":x4,"y":y4,"z":z4}

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
offset = .4

xParaBounds = 9
yParaBounds = 7

# bellow will draw points where the parabolic mesh should be top left, top right, center, bottom right, and bottom left points
ax.scatter(doex, doey, doez, color='blue')
ax.scatter(doex[0],((doey[0]+doey[1])/2),((doez[0]+doez[2])/2),color='blue')

xi = np.linspace(-5.5, 6.5, 500)
yi = .03*xi**2
yii = (((-xi*math.cos(theta)+yi*math.sin(theta)-h)**2)+k)

# second plot of the parabola off to the side of the hoop
xii = np.linspace(-5.5,6.5,500)
yii = .03*xii**2
yiii = (((-xi*math.cos(theta)+yi*math.sin(theta)-h)**2)+k)

xiii = np.linspace(-5.5,6.5,500)
yiiii = .03*xii**2
yiiiii = (((-xi*math.cos(theta)+yi*math.sin(theta)-h)**2)+k)

########
xip = np.linspace(0, 10, 500)
yip = .09*-xip**2+12

# ax.plot(xip+offset,yip+1.5,10,zdir='y',color='black')
# ax.plot(xip,yip,10,zdir='y',color='black')
########

# csvData = csvTool.readCsv('test1.csv',',')
# print(csvData)

guess = (1,1)
#draw hoop, arrays are for x, y location on the graph
backboard=[5,11.5]
xy=[2,10]
#hoop location parameters
circlexy=[2.25,6.5]
# x = para.X(0,15)
# s = para.parabolic(.3,0,12,x)

b = Rectangle(backboard,3,2.25,fill=False,color='red')
c = Circle((circlexy),radius=2.25,fill=False)
#72 - 9 48 - 6 
p = Rectangle(xy,9,6,edgecolor='red',facecolor='none')

# to get vertex of the parabola index at 0 so xip[len(xip)-(len(xip))],yip[len(yip)-(len(yip))]+OFFSET will result in locating index 0
# use this in automated fashion to get the vertex and calculate bounce angle

x1 = circlexy[0]
y1 = circlexy[1]
z1 = 10

# x2 = xip[len(xip)-(len(xip))]+offset
# y2 = yip[len(yip)-(len(yip))]-2
# z2 = 13

# ax.plot(randParaX+offset,randParaY+1.5,randZ,zdir="y",color='black')

#X
# ax.plot((yiiii+offset)-.5,.5*xiii+((doez[0]+doez[2])/2)-.25,((doey[1])+xParaBounds),zdir='y',color='green')
# ax.plot((yiiii+offset)-.5,.5*xiii+((doez[0]+doez[2])/2)-.25,((doey[1])+(xParaBounds-9)),zdir='y',color='green')

#Y
# ax.plot((yi+offset)-.5,.765*-xi+((doey[0]+doey[1])/2)+.25,(doez[2]+(yParaBounds-13)),zdir='z',color='green')
# ax.plot((yii+offset)-.5,.765*-xi+((doey[0]+doey[1])/2)+.25,(doez[2]),zdir='z',color='green')

'''
Need a random player generator that contains values like launch angle (theta), inital velocity
'''

## player stats
playerHeight = (yip[len(yip)-1]-yip[len(yip)-1]+1.5)/2
ax.scatter(xip[len(xip)-1]+offset,playerHeight,10,zdir='y',color='purple')

playerData = player(45,90)



########
#this helps randomize and prove that boundry detection is working
#Going to ultimatly use the monte calo method to do this

# for l in range(0,20):
rand = random_time(x1,y1,z1)
    # print(rand['x'][0],rand['y'][0],rand['z'][0])
csvTool.outputCsv({'xbound':rand['x'][0],'ybound':rand['y'][0],'zbound':rand['z'][0]})

ax.scatter(x1,y1,z1,zdir='z',color='purple')
########

g1.draw(ax,b,p,c)
plt.show()
importlib.reload(plt)
