# In slicing you can accsess the element of numpy array in range

# We can also define the step, like this: [start:end:step]. ( if you don't give the step than take a 1) (end is not consider end-1 is consider)

import numpy as np


# **** Sclicing in 1D array

arr = np.array([1,2,3,4])

print(arr)

print(arr[0:2])
print(arr[-3:-1])
print(arr[-3:])
print(arr[:2])

# step in the slicing
print(arr[1:5:1])
print(arr[1:5:2]) # This is one element is skip 

# Reverse of the array
print(arr[-1::-1]) # step in negative side


# ***** Slicing in 2D array

arr2 = np.array([[1,2,4,5],[4,5,8,7]])

print(arr2[0,1:3])
print(arr2[1,1:3])
print(arr2[0,:])
print(arr2[1,:-1])







