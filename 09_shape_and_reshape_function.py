import numpy as np

# ****** shape - used for find the shape of the numpy array or find the numbers of rows, columns ,and layers


a = np.array([1,2,3,4]) # 1D Array
print(a.shape)

b = np.array([[1,2,3,4],[1,2,3,4]]) # 2D array
print(b.shape)
print(b.ndim)


# ****** reshape(value) - used for reshape the numpy array using this function or you can covert one dimension to another dimension
# Note - Your array number of element is same as a multiplication of the reshape function value(number of element is required same as a reshape value)

# 1D to 2D
c = np.array([1,2,3,4,5,6])

arr2 = c.reshape(2,3) 

print(c)
print(arr2)
print(arr2.shape)

#  1D  to 3D
d = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

arr3 = d.reshape(2 ,3 ,2)

print(d)
print(arr3)
print(arr3.shape)

# 2D  to 3D 
e = np.array([[1,2,3,4,5,6,7,8,9,10,11,12],[1,2,3,4,5,6,7,8,9,10,11,12]])

arr3 = e.reshape(2 ,3 ,4)

print(e)
print(arr3)

# any dimension of the array into the 1D array
f = np.array([[1,2,3,4,5,6,7,8,9,10,11,12],[1,2,3,4,5,6,7,8,9,10,11,12]])

arr3 = f.reshape(-1)

print(f)
print(arr3)
