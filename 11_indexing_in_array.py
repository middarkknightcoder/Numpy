# In array indexing is two type positive and negative 

import numpy as np

# ******* 1D array 

arr = np.array([1,2,3,4,5])
print(arr)
print(arr.ndim)
print(arr.shape)

# Positive index
print(arr[2])

# Negative index
print(arr[-1]) 
print(arr[-5])


# ******* 2D array (In 2d array you can accsess the element using the rows and column)

print()

arr2 = np.array([[1,2,5,8],[1,2,5,4]])

print(arr2)
print(arr2.ndim)
print(arr2.shape)

# Positive index
print(arr2[0,1])
print(arr2[1,2])

# Negative index
print(arr2[-1,-1])
print(arr2[-1,-2])

# Negative and positive both
print(arr2[-1,0])


# ****** 3D array (In 3D array for accsessing the element by the rows,colunm and layer)

print()

arr3 = np.array([[[1,2,5,4] ,[5,7,8,7]]])

print(arr3)
print(arr3.ndim)
print(arr3.shape)

print(arr3[0,1 ,2]) # arr3[layer ,row ,column]









 
