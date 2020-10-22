from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
import parabolic as para

fig = plt.figure()
ax = plt.axes(projection="3d")

#draw hoop, arrays are for x, y location on the graph
backboard=[12.8,11.5]
xy=[10,10]

x = para.X(0,50)
#we are using a 1:8 scale for everything 
#24 - 3 18 - 2.25 
b = Rectangle(backboard,3,2.25,color='r')
#72 - 9 48 - 6 
p = Rectangle(xy,9,6,edgecolor='black',facecolor='none')

s = para.parabolic(1,1,10,x)

#adding shape to scene
ax.add_patch(b)
ax.add_patch(p)

art3d.pathpatch_2d_to_3d(b, z=0, zdir="x")
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")

ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_zlim(0, 20)

ax.plot(x,s,zdir="y")

plt.show()