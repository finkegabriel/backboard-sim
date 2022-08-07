import numpy as np
from scipy.ndimage.interpolation import rotate

doex = np.array([.4,.4,.4,.4])
doey = np.array([11,2,2,11])
doez = np.array([9.9,9.9,15.9,15.9])

rotated = rotate((doex,doey,doez),angle=90)

print(rotated)