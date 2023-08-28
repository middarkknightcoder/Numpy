# Here we are create the random number array using the some numpy functions

# ***** random - is a one type of class or keyword which is used for the create when you need to create the rand number array

import numpy as np

# ***** rand() - function is used for the create the random number array between 0 and 1

# arr_rand = np.random.rand(5)
# print(arr_rand)


# arr2_rand = np.random.rand(3,4)
# print(arr2_rand)


# ***** randn() - function is used for the create the random number array close to zero and both positive and negative

# arr_randn = np.random.randn(4)
# print(arr_randn)

# arr2_randn = np.random.randn(3,4)
# print(arr2_randn)


# ***** randf() - function is used for the create the random number array with floating value which is [0.0 ,1.0) 
# take only one positional arguments

# arr_ranf = np.random.ranf(4)
# print(arr_ranf)

# arr2_ranf = np.random.ranf([3,4])
# print(arr2_ranf)


# ***** randint() - function is used for the create the random number array between the given range

arr_randint = np.random.randint(0 ,20 ,5) # (minrange ,maxrange ,totalNumber)
print(arr_randint)


# ****** Choice(array ,size=value) - used for the generate the random value into the array

random_num = np.random.choice([4,7,8,5,2,6])
print(random_num)

random_array = np.random.choice([7,5,8,9,5,2,3] ,size=(2,3))
print(random_array)
