import numpy as np

# **** insert(array_name ,position ,value) - used for the insert the value into specified position

a = np.array([1,5,4,7,8,5,2])

print(a)

new_a = np.insert(a ,2 ,50)
print(new_a)

new_a2 = np.insert(a ,(2,5),80)
print(new_a2)

# You can also insert the element into the 2D array

b = np.array([[1,2,5],[4,5,9]])

print(b)

new_b = np.insert(b ,2 ,90)
print(new_b)

new_b1 = np.insert(b ,2 ,20 ,axis=0) # inesert the new row with enterd element
print(new_b1)

new_b2 = np.insert(b ,2 ,90 ,axis=1)
print(new_b2)

# **** append(array_name ,value) - used for the append(insert) the element at the end of the array

c = np.array([1,2,5,4,7])

print(c)

new_c = np.append(c ,8)
print(new_c)


# **** delete(array_name ,position) - used for the delete the array element at the specifid position

d = np.array([1,2,5,8,7])

new_d = np.delete(d,4)
print(new_d)

new_d1 = np.delete(d,np.where(d == np.max(d)))  # You can also find the index using the where function
print(new_d1)

