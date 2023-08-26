# Brodcasting - In this type of operation artithmetic operation is also perform where shape is diffrent 
# In broadcasting you need to check the rows and column are same or not

import numpy as np

a1 = np.array([[1],[2],[3]]) # This is (3,1)
print(a1.shape)

a2 = np.array([1,2,3]) # This is (1,3)
print(a2.shape)

print(a1 + a2)




