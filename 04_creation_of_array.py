# array() - used for creat the array using the numpy
# arrayName.ndim() - used for the find dimensionl of the array

import numpy as np

# ****** zero D array 

# ar0 = np.array(5)
# print(ar0)
# print(ar0.ndim)


# ******* one D array

# ar1 = np.array([1,2,4,5]) 
# print(ar1)
# print(ar1.ndim)

# ******** two D array

# ar2 = np.array([[1,2,4,5] ,[3,4,5,6]]) # you can add many list with same number of element
# print(ar2)
# print(ar2.ndim)


# ******** three D array

ar3 = np.array([[[1,2,4,5] ,[3,4,5,6]],[[1,2,4,5] ,[3,4,5,6]]]) # you can add many list with same number of element
print(ar3)
print(ar3.ndim)


# ******** higer or n D array

arn = np.array([[2,3,4,5,6] ,[2,3,4,5,6]] ,ndmin = 5) # you can add many list with smae number of element
print(arn)
print(arn.ndim)


# This is throw the error
# ar3 = np.array([[[[1,2,4,5],[1,2,4,5]] ,[3,4,5,6]]]) # you can add many list with same number of element
# print(ar3)
# print(ar3.ndim)