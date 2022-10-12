import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
xy = arr.view()
print(arr)
print(x)
print(xy)
print(x.base)
print(xy.base)