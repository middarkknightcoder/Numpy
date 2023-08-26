''' 
    %timeit - function used for the check execution time of one line code in python
    %%timeit - function used for the check execution time of whole program in python
'''


import timeit as ti
import numpy as np
 

print(ti.timeit(stmt = "[j**4 for j in range(1 ,9)]"))

print(ti.timeit(stmt = "np.arange(1 ,9)**4"))