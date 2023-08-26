import numpy as np

# Copy - used for the copy array element into the new array
# Note : If you can change the any element of the original array then not reflect(not change) the copyed array and viseversa

arr = np.array([1,2,3,5])
arr_copy = arr.copy()

arr[1] = 20

print(arr)
print(arr_copy)

print()

# views - used for the copy array element into the new array
# Note : If you can change the any element of the original array then reflect(change occures) the copyed array (means original and copyed array is connected because you can only view array element into the new array)

ar = np.array([1,2,5,4,7])
ar_view = ar.view()

print(ar)
print(ar_view)
