from tkinter import Y
from mpl_toolkits.mplot3d import Axes3D
from parabolic import X
from scipy.ndimage.interpolation import rotate
import mpl_toolkits.mplot3d.art3d as art3d
import csvfile as csv
import mpl_toolkits.mplot3d.art3d as art3d

class Graph():
    def draw(self,ax,b,p,c):
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
