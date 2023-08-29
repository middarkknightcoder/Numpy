# Join - you can create the one array using the two or more than two array
# For the join we are used the concatenate() and stack() functoion

import numpy as np

# ****** concatenate() Function to join

# concatenate(array_names) - used for the join the two or more array 
# concatenate(array_names,axis=value) is used the axis which is for used how your array is join

# 1D array
a1 = np.array([1,2,3,4])
a2 = np.array([6,7,8,9])

a = np.concatenate((a1,a2))
print(a)

# 2D array
b1 = np.array([[1,2,3,4],[5,6,7,8]])
b2 = np.array([[1,2,3,10],[5,6,7,20]])

b = np.concatenate((b1,b2),axis=0)  # axis 0 is varticaly
print(b)

b = np.concatenate((b1,b2),axis=1) # axis 1 is horizontaly
print(b)

print()
print("Stack Function")

# ****** stack() Function to join
# stack() - used for the join the two or more than two array into the one array also you can join the using rows ,column and hight


c1 = np.array([1,2,3,4])
c2 = np.array([6,7,8,9])

c = np.stack((c1,c2))
print(c)

ch = np.hstack((c1,c2)) # Join the horizontaly by row wise 1d array
print(ch)

cv = np.vstack((c1,c2)) # join the verticaly by column wise 2d array
print(cv)

cd = np.dstack((c1,c2)) # join the verticaly by column wise 3d array
print(cd)

print()
print()

# ----------------------------------------------------------------------------------------------------------------------------------

# split - used for the split one array to multiple array
# array_split(array_name ,number_of_spliting) - used for the spliting and you need to give a numer how many type you need to split


# ***** 1D array spliting 

arr = np.array([1,2,3,4,5,6])

newArr = np.array_split(arr,4)
Arr = np.array_split(arr,8)

print(newArr) 
print(Arr) 
print(type(newArr))

# Here newArr is a list so you can accsess the element by using the index

print(newArr[0])
print(newArr[1])
print(newArr[2])
print(newArr[3])


# 2D array spliting

arr2d = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])

newArr2d_1 = np.array_split(arr2d,2,axis=1) # split veriticaly  by column 
newArr2d_0 = np.array_split(arr2d,2,axis=0) # split veriticaly  by rows 

newArrh = np.hsplit(arr2d,2) # split by column

print(newArr2d_1)
print(newArr2d_0)

print()
print(newArrh)













