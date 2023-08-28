# log - is logerithm of the array element using the universal function
# log2(log base 2) ,log10(log base 10) ,log(log base e) ,logn(log base n) 

# Note : In python we are used math.log(value ,base) function for find the logerithm value 

import numpy as np

# **** log10(arr) - we are finding the value of the array element with log base 10

a = np.arange(1,11)
print(a)
log10_a = np.log10(a)
print("The array element log base 10 value is : \n",log10_a)

print()

# **** log2(arr) - we are finding the value of the array element with log base 2

b = np.arange(1,11)
print(b)
log2_b = np.log2(b)
print("The array element log base 2 value is : \n",log2_b)

print()

# **** log(arr) or natural log - we are finding the value of the array element with log base e

c = np.arange(1,11)
print(c)
loge_c = np.log(c)
print("The array element log base e value is : \n",loge_c)

print()

# **** log at any base - we are finding the value of the array element with any base of log
# Note : NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:

from math import log   # Here log is a function

logn = np.frompyfunc(log ,2 ,1)

print("The array element log base n value is : \n" ,logn([1,2,3,4,5,6,7,8,9] ,15))   #logn(value ,base)





