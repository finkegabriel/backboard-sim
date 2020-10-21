from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import mpl_toolkits.mplot3d.art3d as art3d

fig = plt.figure()
ax = plt.axes(projection="3d")

#draw hoop, arrays are for x, y location on the graph
backboard=[1.75,3.25]
xy=[1.5,3]
b = Rectangle(backboard,.5,.5,color='r')
p = Rectangle(xy,1,1,edgecolor='black',facecolor='none')

#adding shape to scene
ax.add_patch(b)
ax.add_patch(p)

art3d.pathpatch_2d_to_3d(b, z=0, zdir="x")
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")

ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

plt.show()