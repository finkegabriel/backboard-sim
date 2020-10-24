from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle,Circle
from matplotlib.text import TextPath
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.animation as animation
import parabolic as para

fig = plt.figure()
ax = plt.axes(projection="3d")

#draw hoop, arrays are for x, y location on the graph
backboard=[-2,11.5]
xy=[-5,10]
circlexy=[2.25,-.5]

x = para.X(0,15)

#we are using a 1:8 scale for everything 
#24 - 3 18 - 2.25 
b = Rectangle(backboard,3,2.25,color='red')
c = Circle((circlexy),radius=2.25,fill=False)
#72 - 9 48 - 6 
p = Rectangle(xy,9,6,edgecolor='red',facecolor='none')

s = para.parabolic(.2,0,12,x)

#adding shape to scene
ax.add_patch(b)
ax.add_patch(p)
ax.add_patch(c)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

art3d.pathpatch_2d_to_3d(b, z=0, zdir="x")
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
art3d.pathpatch_2d_to_3d(c, z=10, zdir="z")

ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_zlim(0, 20)

#zs moves along the z axis that we define in this case being y
ax.plot(x,s,zs=2,zdir="y")

para.finalX(10,5)

plt.show()
