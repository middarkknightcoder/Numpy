# Many Types of data type is exist in a numpy array
# dtype - keyword is used for the find the data type of the numpy array because we are know numpy array is stored only same type of data type

import numpy as np

a = np.array([1,2,3,4]) # This is int32
print(a.dtype)

b = np.array([1.2,5.2,1.5,4.5]) # This is float64
print(b.dtype)

c = np.array(["a","b","c","d"]) # This is a unsign data type <U1
print(c.dtype)

d = np.array(["a",4 ,5.2,2]) # This is a unsign data type also but <U32
print(d.dtype)


# You can also change the data type of the numpy array using the dtype with np data types value

e = np.array([1,2,3,4] ,dtype = np.int8) # This data type is exist into the numpy library
print(e.dtype)
print(e)


# You can also change the data types of the numpy array using the dtype with short form word as a value

f = np.array([1,2,3,4] ,dtype = "f") # Change into the float32 
print(f.dtype)
print(f)

g = np.array([1,2,3,4] ,dtype = "S") # Change into the string |S1
print(g.dtype)
print(g)


# You can also change the data type of the numpy array using the numpy lib data types as a function

h = np.array([1,2,3,4])

newh = np.float32(h)

newoneh = np.int_(newh)

print(h.dtype)
print(h)

print(newh.dtype)
print(newh)

print(newoneh.dtype)
print(newoneh)


# You can also change the data type of the numpy array using the astype() function

i = np.array([1.5,2.0,3.6,7.7])

newi = i.astype(int)

print(i.dtype)
print(i)

print(newi.dtype)
print(newi)


# Note : Some array data types is not convertable like you can not conver string dtype into the int dtype

