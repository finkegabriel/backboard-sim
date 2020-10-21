from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
import parabolic as para

fig = plt.figure()
ax = plt.axes(projection="3d")

#draw hoop, arrays are for x, y location on the graph
backboard=[24,132]
xy=[0,120]

#we are using a 1:1 scale for everything 
b = Rectangle(backboard,24,18,color='r')
p = Rectangle(xy,72,48,edgecolor='black',facecolor='none')

#adding shape to scene
ax.add_patch(b)
ax.add_patch(p)

art3d.pathpatch_2d_to_3d(b, z=0, zdir="x")
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")


ax.set_xlim(0, 1128)
ax.set_ylim(0, 90)
ax.set_zlim(0, 90)

print(para.parabolic(1,10,100,11))

plt.show()