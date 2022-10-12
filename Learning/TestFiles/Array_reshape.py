import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a=a.reshape(3,4)
print(a)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)