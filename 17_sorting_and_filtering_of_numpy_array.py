# sorting - is a techniqe which  is used for the sorting the element of the numpy array
# Filtering - is a techniqe which is used for the filtering(skip) the element into the numpy array

# ******* np.sort(array_name) : used for the sorting the array element

import numpy as np

a1 = np.array([1,5,8,7,6,11,54,25])
print(np.sort(a1))

# Soring the string also (sorting by the ascci value)

a2 = np.array(["r" ,"joker", "back"])
print(np.sort(a2))


# ******* Filter(value) : Used for the filtering the element into the array In filtering we ara used the boolean value

a3 = np.array([1,5,8,9,5])

a_filter = [True ,False ,True ,True ,False]
x1 = a3[a_filter]
print(x1)

# You can also used the for loop for the filtering

a4 = np.array([12,54,75,65,45,12,35])

a_filter = []

for i in range(0 ,len(a4)):
    
    if(a4[i] >50):
        a_filter.append(True)
    else:
        a_filter.append(False)
        
print(a4[a_filter])



    






