from matplotlib.patches import Rectangle,Circle
from translate import Translate
from graph import Graph
import matplotlib.pyplot as plt
import numpy as np
import parabolic as para
import importlib

t1 = Translate()
g1 = Graph()
ax = plt.axes(projection="3d")

#draw hoop, arrays are for x, y location on the graph
backboard=[-2,11.5]
xy=[-5,10]
#hoop location parameters
circlexy=[2.25,-.5]
x = para.X(0,15)
s = para.parabolic(.3,0,12,x)

b = Rectangle(backboard,3,2.25,fill=False,color='red')
c = Circle((circlexy),radius=2.25,fill=False)
#72 - 9 48 - 6 
p = Rectangle(xy,9,6,edgecolor='red',facecolor='none')

for _ in range(0,1): #for loop to create multiple parabolas instances
    z = para.z(x,s,_)
    ax.plot(x,s,'b--',zs=z,zdir="y")

g1.draw(ax,b,p,c)
# g1.plot3D(ax,x1,y1,z1)
plt.show()
importlib.reload(plt) 