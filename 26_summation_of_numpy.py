# diffrence between summation and addition is Addition perform between two number where summation perform on n number

import numpy as np

# ***** Addition 

a = np.array([1,2,5,7,8])
b = np.array([7,8,5,9,3])

add_arr = np.add(a,b)

print(add_arr)


# ***** Summation 

sum_arr = np.sum([a,b])  # If you don't used the [] then throw error - only integer scalar arrays can be converted to a scalar index

print(sum_arr)


# Summation over an axis

sum_arr_ax1 = np.sum([a,b] ,axis=1)
print(sum_arr_ax1)

sum_arr_ax0 = np.sum([a,b] ,axis=0) # This is same as a addition
print(sum_arr_ax0)

# Cummulative summation - In cummulative sum partialy adding element of array
# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

cum_sum = np.cumsum(a)
print(cum_sum)


