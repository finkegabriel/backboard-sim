from mpl_toolkits.mplot3d import Axes3D
from scipy.ndimage.interpolation import rotate
from matplotlib.patches import Rectangle,Circle
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
import parabolic as para
import numpy as np
import csvfile as csv

fig = plt.figure()
ax = plt.axes(projection="3d")

# generate x and y values then to compute z do this z = x^2-y^2


#draw hoop, arrays are for x, y location on the graph
backboard=[-2,11.5]
xy=[-5,10]
#hoop location parameters
circlexy=[2.25,-.5]

#this is the domain for the parabolic function
x = para.X(-15,15)

#we are using a 1:8 scale for everything 
#24 - 3 18 - 2.25 
b = Rectangle(backboard,3,2.25,color='red')
c = Circle((circlexy),radius=2.25,fill=False)
#72 - 9 48 - 6 
p = Rectangle(xy,9,6,edgecolor='red',facecolor='none')

s = para.parabolic(.3,0,12,x)

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
##############,zs=x

ax.plot(x,s,'b--',zs=1,zdir="y")
# ax.plot(x,s2,'b--',zs=za,zdir="z")

plt.show()