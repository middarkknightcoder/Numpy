# Permutation - means arrengment of the array in diffrent way (npr) - Order is matter in permutation
# For random permutation of array we are used to method : Shuffle() and permutation()

import numpy as np

# ****** Shuffle(array) - it's change the orginal array with shuffle

arrs = np.array([1,2,5,7,8])
np.random.shuffle(arrs)
print("Array randomly arrange with the shuffle : ",arrs)

# ****** permutation(array) - it's do't change the original array with permuatation

arrp = np.array([1,2,5,7,8])
np.random.permutation(arrp)
print("Array arrange with the permutation original array : ",arrp)
print("Array is arrange using the permutation function : ",np.random.permutation(arrp))

