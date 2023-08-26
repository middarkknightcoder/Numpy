# You can perform the arithmetic operation using the sign and universal function of numpy 
# EX : arr = arr1 + arr2 & arr = np.add(arr1 ,arr2)

# Types of operation into the numpy array :-
# a + b    or   np.add(a,b)
# a - b    or   np.subtract(a,b)
# a * b    or   np.multiply(a,b)
# a / b    or   np.divide(a,b)
# a % b    or   np.mod(a,b)
# a ** b    or   np.power(a,b)
#  1/a and 1/b    or   np.reciprocal(a,b)


import numpy as np

# ***** Addition operation in 1d array

# used Sign for the Arithmetic operation
arr1 = np.array([1,2,3,4])
arr = arr1 + 2 # Here we are perform the addition operation with the number 
print(arr)

arr2 = np.array([1,2,3,4])
arr = arr1 + arr2
print(arr)

# used function for the arithmetic operation

arrf = np.add(arr1 ,arr2)
print(arrf)

arrf = np.add(arr1 ,4)
print(arrf)


# ****** addtion operation in 2d operation
print()

# used Sign for the Arithmetic operation
arr1 = np.array([[1,2,3,4],[1,2,3,4]])
arr = arr1 + 2 # Here we are perform the addition operation with the number 
print(arr)

arr2 = np.array([[1,2,3,4],[1,2,3,4]])
arr = arr1 + arr2
print(arr)

# used function for the arithmetic operation

arrf = np.add(arr1 ,arr2)
print(arrf)

arrf = np.add(arr1 ,4)
print(arrf)



# ******* module operation in 1d array

print()

arr1 = np.array([1,2,3,4])
arr = arr1 % 3 # Here we are perform the addition operation with the number 
print(arr)

arr2 = np.array([4,2,3,4])
arr = arr1 % arr2
print(arr)

# used function for the arithmetic operation

arrf = np.mod(arr1 ,arr2)
print(arrf)

arrf = np.mod(arr1 ,4)
print(arrf)


# ****** module operation in 2d operation
print()

# used Sign for the Arithmetic operation
arr1 = np.array([[1,2,3,4],[1,2,3,4]])
arr = arr1 % 2 # Here we are perform the addition operation with the number 
print(arr)

arr2 = np.array([[1,2,3,4],[1,2,3,4]])
arr = arr1 % arr2
print(arr)

# used function for the arithmetic operation

arrf = np.mod(arr1 ,arr2)
print(arrf)

arrf = np.mod(arr1 ,4)
print(arrf)


# ******* power operation in 1d array (sing of power is **)

print()

arr1 = np.array([1,2,3,4])
arr = arr1 ** 3 # Here we are perform the addition operation with the number 
print(arr)

arr2 = np.array([1,2,3,4])
arr = arr1 ** arr2
print(arr)

# used function for the arithmetic operation

arrf = np.power(arr1 ,arr2)
print(arrf)

arrf = np.power(arr1 ,4)
print(arrf)


# ****** power operation in 2d operation
print()

# used Sign for the Arithmetic operation
arr1 = np.array([[1,2,3,4],[1,2,3,4]])
arr = arr1 ** 2 # Here we are perform the addition operation with the number 
print(arr)

arr2 = np.array([[1,2,3,4],[1,2,3,4]])
arr = arr1 ** arr2
print(arr)

# used function for the arithmetic operation

arrf = np.power(arr1 ,arr2)
print(arrf)

arrf = np.power(arr1 ,4)
print(arrf)

# ***** absolute() - function is used for the niglet the sign of the array element 

ar = np.array([-1,4,-2,5,-9,3])

print(np.absolute(ar))


# ***** Note : You can perform the all ohter type of AO operation same as above operation

# Also You can perform the any type of operation into the any dimensional array

