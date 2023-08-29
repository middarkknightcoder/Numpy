# ufunc - Universal function which is used for the operation with the ndarray
# It's provide the vectorization in numpy array and very help full in numpy operation

import numpy as np

# ***** zip() function is zip the variable without using the ufunc you need a fir loop

a1 = np.array([4,5,2,3,6,8])
a2 = np.array([1,4,7,5,2,3])


for i,j in zip(a1,a2): # If you don not use zip() then throw error too many values to unpack (expected 2)
    print(i+j)
    
# ***** using the ufunc for the operation of the addition (addition with vwctorization)

print(np.add(a1,a2))


# ****** Create Your own ufunc
# Note : when you create your own ufunc so you need to add in numpy library for the use in your program 

# frompyfunc(function ,number of input ,number of output)

def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd ,2 ,1) # Add into np library

print("Addition using the own created ufunc : ",myadd([1,4,5,8,7],[7,5,6,5,2]))
print(type(myadd))

print("Check the given function is ufunc or not : ",type(myadd) == np.ufunc)


# Note : You can perform arithmetic operation using the ufunc (check program number 08)
