from matplotlib.patches import Rectangle,Circle
from translate import Translate
from graph import Graph
import matplotlib.pyplot as plt
import numpy as np

t1 = Translate()
g1 = Graph()
g2 = Graph()
ax = plt.axes(projection="3d")

#draw hoop, arrays are for x, y location on the graph
backboard=[-2,11.5]
xy=[-5,10]
#hoop location parameters
circlexy=[2.25,-.5]

x1 = [0,1,3,4,5,6]
y1 = [0,1,2,3,4,5]
z1 = [0,1,2,3,4,5]

x2 = [-1,0,1,2,3,4]
y2 = [-1,0,1,2,3,4]
z2 = [-1,0,1,2,3,4]

b = Rectangle(backboard,3,2.25,fill=False,color='red')
c = Circle((circlexy),radius=2.25,fill=False)
#72 - 9 48 - 6 
p = Rectangle(xy,9,6,edgecolor='red',facecolor='none')

print("x","y","z")
g1.draw(ax,b,p,c)
g1.plot3D(ax,x1,y1,z1)
# g2.draw(ax,np.array(b),np.array(p),np.array(c))