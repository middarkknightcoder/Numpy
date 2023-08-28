import numpy as np

# uniqe() - used for the find the set into the array

arr = np.array([1,4,5,2,1,4,2,1])

x = np.unique(arr)
print("Uniqe array : ",x)


# Union - Find the uniqe value into the both set

s1 = np.array([1,4,5,2,1])
s2 = np.array([2,8,7,5])

s_union = np.union1d(s1 ,s2)
print("Union of the value : ",s_union)


# intersection - Find the value which is same in both

s_inter = np.intersect1d(s1,s2 ,assume_unique=True)  # assume_uniqe is a optional argu it's used for the speedup the computational speed
print("Intersection of array : ",s_inter)


# diffrence - To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method. (s1 - s2 = s1 - (s1 intersect s2))

s_diff = np.setdiff1d(s1 ,s2 ,assume_unique=True)
print("Diffrence of array : ",s_diff)

# Symmetric diffrence - To find only the values that are NOT present in BOTH sets, use the setxor1d() method.

s_sydiff = np.setxor1d(s1 ,s2 ,assume_unique=True)
print("Symmetric Diffrence : " ,s_sydiff)

