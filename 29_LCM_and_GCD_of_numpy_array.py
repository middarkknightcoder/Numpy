import numpy as np

# ****** Lowest common multiple - lcm is a common multiple of the two number

n1 = 9
n2 = 4

print("The given two number lcm is : ",np.lcm(n1 ,n2)) # 9*4 = 36 & 4*9 = 36

# np.lcm.reduce() - used for the find the lcm of the array element

arr = np.array([4,5,8,7,3])

print("The lcm of the all array element is : ",np.lcm.reduce(arr))


# ****** Greteast common denominator or higest common factor - used for the find the two or more number common denominator

print("Thwe given two number gcd is : ", np.gcd(n1,n2)) # 9/1 = 9 & 4/1 = 4 so gcd is 1


# np.gcd.reduce() - used for the find the gcd of the array element

print("The gcd of the array element is : ",np.gcd.reduce(arr))



