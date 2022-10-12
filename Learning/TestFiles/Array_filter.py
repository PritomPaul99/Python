import numpy as np
a=np.array([1,2,3,4,5])

filter=[]
#create a empty list
for x in a:
    if x%2==0:
        filter.append(False)
    else :
        filter.append(True)

new_a=a[filter]

print(new_a)
