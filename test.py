import matplotlib.pyplot as plt
import numpy as np
import math as math

# create 1000 equally spaced points between -10 and 10
x = np.linspace(-10,10, 1000)
rotate = math.degrees(1.7)
# calculate the y value for each element of the x vector
y = x**2
yii = ((x*math.cos(rotate))+(y*math.sin(rotate)))

print("rotated ")

fig, ax = plt.subplots()
plt.ylim([-30,30])
plt.xlim([-10,30])
ax.plot(x, yii)
plt.show()