from numpy import random
x=random.randint(100)
print(x)

#Generate a random float from 0 to 1:
x=random.rand()
print(x)

#Generate a 1-D array containing 5 random integers from 0 to 100:

from numpy import random

x=random.randint(100, size=(5))

print(x)

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

from numpy import random

x = random.randint(100, size=(3, 5))

print(x)

#generate five random number

from numpy import random

x = random.rand(5)

print(x)


#The choice() method takes an array as a parameter and randomly returns one of the values.



from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)


#The choice() method also allows you to return an array of values.

#Add a size parameter to specify the shape of the array.

#Example
#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)