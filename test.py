from matplotlib import pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
x, y, z = [1, 1.5], [1, 2.4], [3.4, 1.4]
ax.scatter(x, y, z, c='red', s=100)
ax.plot(x, y, z, color='black')
plt.show()