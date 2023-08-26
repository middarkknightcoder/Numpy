# itreting - iterating is one type of method which is print the element of an array in sepratly
# You can itrate the array in two ways 1.loops only 2.np.nditre(array_name) function

import numpy as np

# ****** 1D array itreting

arr1 = np.array([1,2,3,4,5,6])

print(arr1)

# Using loop
for i in arr1:
    print(i)

print()

# Using numpy function
for i in np.nditer(arr1):
    print(i)
for i in np.nditer(arr1 ,flags = ["buffered"] ,op_dtypes=["S"]): # You can also stored into the buffered in string form
    print(i)

# Iterating with the index using the np.ndenumerate(array_name)
for i,j in np.ndenumerate(arr1):
    print(i, j)

print()
print()


# ****** 2D array itreting

arr2 = np.array([[1,2,5,4],[4,5,8,7]])

print(arr2)

# Using loop
for i in arr2:
    for j in i:
        print(j)
        
print()

# Using numpy function
for i in np.nditer(arr2):
    print(i)
    
# Iterating with the index using the np.ndenumerate(array_name)
for i,j in np.ndenumerate(arr2):
    print(i, j)

print()
print()

# ***** 3D array iterating

arr3 = np.array([[[1,2,5,4],[9,5,7,8]]])

# Using Loops
for i in arr3:
    for j in i:
        for k in j:
            print(k)
            
print()  

# Using iteration function
for i in np.nditer(arr3):
    print(i)
    
# Iterating with the index using the np.ndenumerate(array_name)
for i,j in np.ndenumerate(arr3):
    print(i, j)
