# import matplotlib.pyplot as plt

# X = [1,2,3,4,5,6,7,8,9,10]
# Y = [10,9,8,7,6,5,4,3,2,1]

# for x,y in zip(X, Y):
#     x1 = [0, x]
#     y1 = [y, 0]
#     plt.plot(x1, y1)
# plt.show()

import numpy as np

x=np.arange(2)
y=np.arange(3)
[X,Y] = np.meshgrid(x,y)
S=X+Y

print(S.shape)
# (3, 2)
# Note that meshgrid associates y with the 0-axis, and x with the 1-axis.

print(S)
# [[0 1]
#  [1 2]
#  [2 3]]

s=np.empty((3,2))
print(s.shape)
# (3, 2)

# x.shape is (2,).
# y.shape is (3,).
# x's shape is broadcasted to (3,2)
# y varies along the 0-axis, so to get its shape broadcasted, we first upgrade it to
# have shape (3,1), using np.newaxis. Arrays of shape (3,1) can be broadcasted to
# arrays of shape (3,2).
s=x+y[:,np.newaxis]
print(s)
# [[0 1]
#  [1 2]
#  [2 3]]