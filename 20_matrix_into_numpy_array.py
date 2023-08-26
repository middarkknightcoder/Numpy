# Matrix is a well defined collection of the element but matrix is same as a array but operations are change 
# Here we are used the matrix function for createing the matrix into the numpy array (matrix is a alway 2D)

import numpy as np

arr = np.array([[1,2,5],[4,6,8]])
print("This is a 2D array : \n",arr)
print(type(arr))


mat = np.matrix([[1,2,5],[4,7,5]])
print("The numpy matrix : \n",mat)
print(type(mat))

# **** Perform the addition operation in matrix also you can also perform the substraction operation in matrix

mat1 = np.matrix([[1,4],[7,8]])
mat2 = np.matrix([[5,4],[7,5]])

print("The addition of the matrix : \n",mat1 + mat2)
print("The addition of the matrix using the function : \n" ,np.add(mat1,mat2))


# **** Matrix dote product or matrix multiplication(rule : m1(2 x 3) and m2(3 x 2) first(outer) matrix coulmn and second(inner) matrix rows are need to same or Broadcasting )
# mat1.dot(mat2) - used for the matrix multiplication

print("Matrix multiplication using the * : \n",mat1 * mat2)
print("Matrix multiplication using the dot function : \n",mat1.dot(mat2))


# **** Transpose of the matrix (Transpose - rows elements are conerting into the column)

matT = np.matrix([[1,4],[7,8]])

print(matT)
print("Transpose of the matrix : \n",np.transpose(matT))
print()
print("Transpose of the matrix using the T keyword : \n",matT.T)
print()

# ***** swapaxis(matrix ,0,1) - usde for the swap the axis with row to column or column to row 

print(np.swapaxes(matT ,0,1)) 
print(np.swapaxes(matT ,1,0))


# ***** np.linalg.inv(matI) - Inverse of the matrix using the function

matI = np.matrix([[1,2],[3,4]])
print(matI)
print()

print(np.linalg.inv(matI))
print()


# ***** np.linalg.matrix_power(matP ,2) - Power of the matrix using the function

matP = np.matrix([[1,4,5],[7,5,8],[5,8,7]])
print(matP)

print(np.linalg.matrix_power(matP ,2))

 
# ***** np.linalg.det(matD) - Determinat of the matrix is find using the numpy function

matD = np.matrix([[1,4],[7,5]])

print(np.linalg.det(matD))






