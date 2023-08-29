# searching is method which is used for the find the vlaue into the numpy array

import numpy as np

# ****** Where(array with operation = value) - used for the find the index of the numpy array specifind value

arr = np.array([2,4,5,8,7,5,4,9,8,7])

x1 = np.where(arr == 5)
print(x1)

x2 = np.where(arr % 2 == 0)
print(x2)


# ****** searchsort() - There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
# Note : This method is used when sorting array is exist

ar = np.array([1,2,3,5,6,7])

x3 = np.searchsorted(ar ,3) # Here defalut side is "left"

print("The index of the value 3 where we can put the 3 in array",x3)

# You can also give the side= "Right or left"

x3 = np.searchsorted(ar ,4 ,side="right")

print(x3)