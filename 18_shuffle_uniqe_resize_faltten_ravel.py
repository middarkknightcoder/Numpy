import numpy as np

# ***** Shuffle - function is used for the shuffle the element of the array and create the new array

arr = np.array([1,2,5,4,7,9])
np.random.shuffle(arr)

print(arr)


# ***** Unique - function is used for the take a unique element into the array

arr1 = np.array([1,5,4,7,4,9,7])

Uniqe_a = np.unique(arr1 ,return_index=True ,return_counts=True)

print("Uniqe array : " ,Uniqe_a)

# ***** Resize - function is used for the resize of the array 

arr2 = np.array([1,5,4,7,4,9])

resize_a = np.resize(arr2 ,(2,3)) 
resize_a = arr2.reshape(2,3)

print(arr2)
print(resize_a)


# ***** Flatten - function is used for the resize the array into the 1d array

print(resize_a.flatten())
print("Flatten : \n" ,resize_a.flatten(order="F")) # Also you can used the order = {"C(row-major) ,F(column-major) ,A ,K}


# ***** Raval - function is used for the also resize the array into the 1d array - You can also used the above order

print(np.ravel  (resize_a))
print(np.ravel(arr2))

print("Raval : " ,np.ravel(resize_a ,order="F"))







