# In numpy many types of trigonometric functions are exist like , sin() ,cos() and tan()

import numpy as np

print(np.sin(np.pi/2))

# You can put all data into array and after find the sin() value of the all element of the array

arr = np.array([np.pi/2 ,np.pi/4 ,np.pi/6])

print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))
print(np.sin(1.57)) # Pi/2 approx 1

# Note : You can also find the cos and tan value same as above


# ****** Convert degree into the radians and also radians into degree

# Formula : radians = pi/180 * degree_values

a_degree = np.array([90 ,180 ,360 ,270])
a_radians = np.deg2rad(a_degree)
print("The element value in radians is : ",a_radians)

b_radians = np.array([np.pi/2 ,np.pi/4 ,np.pi/6])
b_degree = np.rad2deg(b_radians)
print("The element value in degree is : ",b_degree)


# ***** Finding the angle or inverse value of the sin, cos or tan
# Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).

# Inverse of sin ,cos and tan or angel of value 1 coresponding trigonomatric function
print(np.arcsin(1)) 
print(np.arccos(1))
print(np.arctan(1))

# Find the angle of the array element using arcsin ,arccos and arctan

arr = np.array([1,-1,0.5])

print(np.arcsin(arr))
print(np.arccos(arr))
print(np.arctan(arr))


# ***** Find the hypotenues(karan) using the Pythagoras theorem [(karan0^2 = (base)^2 + (perp)^2)]

base = 15
perp = 20

hypotenues = np.hypot(base ,perp)
print(hypotenues)

