# The diffrence between product and multiplication is multiplication operation doing in the two element where product is operation on the n element

import numpy as np

# ****** Multiplication

a = np.array([1,2,5,4,8])
b = np.array([4,7,5,8,9])

mul_arr = np.multiply(a,b)
print(mul_arr)

# ***** Product of numpy array

prod_arr = np.product([a,b])
print(prod_arr)

# Product using the axis

prod_arr_ax1 = np.product([a,b] ,axis=1)
print(prod_arr_ax1)

prod_arr_ax0 = np.product([a,b] ,axis=0)  # same as a multiplication
print(prod_arr_ax0)

# Cummulative product

cum_prod = np.cumprod(a)
print(cum_prod)

