from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

doex = np.array([0.165,0.165,0.585,0.585])
doey = np.array([ .22, .63, .22, .63])
doez = np.rot90(np.array([ .99, .98,.97,.96]),1)


def paraBolEqn(data,a,b,c,d):
    x,y = data
    return -(((x-b)/a)**2+((y-d)/c)**2)+1.0

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
popt,pcov=optimize.curve_fit(paraBolEqn,np.vstack((doex,doey)),doez,p0=[1.5,0.4,1.5,0.4])

x, y = np.meshgrid(np.linspace(np.min(doex), np.max(doex),10), np.linspace(np.min(doey),np.max(doey), 10))
ax.plot_wireframe(x, y, paraBolEqn((x,y), *popt))
ax.scatter(doex, doey, doez, color='b')

plt.show()