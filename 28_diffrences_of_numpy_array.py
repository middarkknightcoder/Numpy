# Diffrences in the numpy array element and diffrence operation is perform as cummulative substraction

import numpy as np

a = np.array([1,4,5,2,3,6])

diff_arr = np.diff(a)
print(diff_arr)


# You can also give the repatedly parameter n

diff_arr_n = np.diff(a ,n=2) # n=2 means two time operation on array - one is original and after result array 
print(diff_arr_n)




