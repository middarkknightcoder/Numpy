# Numpy provide the hyperbolic function like sinh() ,cosh() and tanh() 

# Formula : 
# sinh(x) = e^x - e^(-x)/2
# cosh(x) = e^x + e^(-x))/2
# tanh(x) = sinh(x) / cosh(x)

# Hyperbolic function take value into the degree form

import numpy as np

x = np.sinh(np.pi/2)
print(x)

arr = np.array([np.pi/2 ,np.pi/4 ,np.pi/3])

arr_sinh = np.sinh(arr)
print(arr_sinh)

arr_cosh = np.cosh(arr)
print(arr_cosh)

print()

# Find the angle for the hyperbolic sin ,cos and tan means find the value of the reverse of the sinh ,cosh and tanh  it's reverse function is arcsinh ,arccosh and arctanh

y = np.arcsinh(1) # arccosh() and arctanh()
print(y)

yrr = np.array([0.4,0.5,0.6])

yrr_arcsinh = np.arcsinh(yrr)
print(yrr_arcsinh)

yrr_arctanh = np.arctanh(yrr)
print(yrr_arctanh)


