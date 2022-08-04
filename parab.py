import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

doex = [0.4,0.165,0.165,0.585,0.585]
doey = [.45, .22, .63, .22, .63]
doez = np.array([1, .99, .98,.97,.96])

def paraBolEqn(data,a,b,c,d):
    x,y = data
    return -(((x-b)/a)**2+((y-d)/c)**2)+1.0

popt,pcov=opt.curve_fit(paraBolEqn,np.vstack((doex,doey)),doez,p0=[1.5,0.4,1.5,0.4])

x, y = np.meshgrid(np.linspace(np.min(doex), np.max(doex),10), np.linspace(np.min(doey),np.max(doey), 10))
ax.plot_wireframe(x, y, paraBolEqn((x,y), *popt))
ax.scatter(doex, doey, doez, color='b')

data = np.vstack((doex,doey))
zdata = doez

opt.curve_fit(paraBolEqn,data,zdata)

plt.show()