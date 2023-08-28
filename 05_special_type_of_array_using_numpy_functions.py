# Here we are create the special type of array using the numpy functions

import numpy as np 

# ***** All Elments are "Zero" in the array

# # This will give you a one d array
# arr_zero = np.zeros(5)
# print(arr_zero)

# # This will give you a two d array
# arr_zero2 = np.zeros([4,5]) # ([rows(x) ,colums(y)])
# print(arr_zero2)

# #This will give you a three d array
# arr_zero3 = np.zeros([4,5 ,2]) #([z(layer) ,x(row) ,y(colum)])
# print(arr_zero3)


# ***** All elements are "one" in array

# arr_one = np.ones(5)
# print(arr_one)

# arr_one2 = np.ones([3,4])
# print(arr_one2)


# ***** Empty array

# arr_emp = np.empty([4 ,3])
# print(arr_emp) # This create the empty arary show in array written priveas content


# ***** array with range of element

# This will give you a one d array
# arr_ran = np.arange(5)
# print(arr_ran)

# # This will give you a two d array
# arr_ran5 = np.arange(5,20)
# print(arr_ran5)


# ***** Digonal "one" only array (identity matrix) - you can only used squre matrix(array)

# arr_dig = np.eye(3 ,3)
# print(arr_dig)


# ***** create array with specified interval - linespace() autometiclly set the interval using the num value

arr_inter = np.linspace(0 ,20 ,num=5) 
print(arr_inter)

arr1_inter = np.linspace(5 ,20 ,num=5)
print(arr1_inter)


