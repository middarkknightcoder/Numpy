# Random number distribution - when you need to destribute the value into the given array we are used the choice(array ,p=[] ,size=value) function
# probability destination function - when you create the array with the randomm number that time which number is reapeted high is dicided by a probability function
# Note : Probability is always between 0 and 1 (in function sum of the probability is 1)

# Ex - When we need to create the random number array with probabily repeatetion

import numpy as np

random_arr = np.random.choice([3,5,6,7,8] ,p=[0.1,0.4,0.3,0.2,0.0] ,size=(10))
print(random_arr) # Pls note high repeatation is number 5 because it's probabilty is high

random_arr2 = np.random.choice([1,2,3,4,5,6] ,p=[0.1,0.2,0.01,0.09,0.4,0.2] ,size=(25))
print(random_arr2)

# You can create the 2d array also 

random_arr2d = np.random.choice([1,2,3,4,5,6] ,p=[0.1,0.2,0.01,0.09,0.4,0.2] ,size=(2,3))
print(random_arr2d)






