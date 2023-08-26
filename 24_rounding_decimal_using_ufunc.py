# Rounding of decimal means one type round of fractional number (Ex: 25.47 [wholenumber decimalpoint fractinalnumber])
# Five way to rounding a decimal in numpy  : truncation ,fix ,rounding ,floor ,ceil

import numpy as np

# ***** trunc(array_name) : Used for remove the fractional part 

a = np.array([-3.578,58.54,2.55,-8.8575])
arr = np.trunc(a)
print("Trucation of the array element : ",arr)


# ***** fix(array_name) : Used for remove the fractional part into the number same as a trnuc

b = np.array([-3.578,58.54,2.55,-8.8575])
brr = np.fix(b)
print("The fixing of the arra element : ",brr)


# ***** around(number ,number of fractional part) : Function is used for the round of the value how many number is exist after the decimal point

c = np.array([3.57785 ,5.47855 ,-54.784])
crr = np.around(c ,2)
print(crr)

print(np.around(-24.57895 ,3)) # You can also round of the single number using the around function


# ***** floor(value) : Used for the find the floor value of the number (Ex : 3.45 Floor value id 3)

d = np.array([4.34 ,5.50 ,-45.333])
drr = np.floor(d)
print("Floor value of the array element : ",drr)


# ***** ceil(value) : Used for the find the ceiling value of the number (Ex : 3.45 ceil value is 4)

e = np.array([4.34 ,5.50 ,-45.333])
err = np.ceil(e)
print("Ceiling value of the array is : " ,err)