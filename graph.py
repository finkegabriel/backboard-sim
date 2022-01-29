from tkinter import Y
from mpl_toolkits.mplot3d import Axes3D
from parabolic import X
from scipy.ndimage.interpolation import rotate
from matplotlib.patches import Rectangle,Circle
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
import csvfile as csv



class Graph():
    def plot3D(self,x,y,z):
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        ax.plot(x,y,z)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()

    def plot2D(self,x,y):
        plt.plot(x,y)
        plt.show()
    
    def save_csv(self,x,y,z):
        csv.exportCsv("data_2.csv",x,y,z)
