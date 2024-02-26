"""
This is to check the performance difference between the numpy array and the list
"""
import time
from copy import deepcopy

# define matrix dimensions
n = 1000

# Create matrices using python list
list1 = [[1 for _ in range(n)] for _ in range(n)]
list2 = deepcopy(list1)

# Start the time
start_time = time.time()

# perform the matrix multiplication
result_list = []

# Iterate through the rows
results = [[0 for _ in range(n)] for _ in range(n)]

for i in range(len(list1)):
    # Iterate through the column
    for j in range(len(list2[0])):
        # Iterate through the row
        for k in range(len(list2)):
            results[i][j] = list1[i][k] + list2[k][j]

elapsed_time = time.time() - start_time

import numpy as np

array1 = np.ones((n,n))
array2 = np.ones((n,n))

# Start time measurement
start_time = time.time()

# Perform matrix multiplication
result_array = np.dot(array1, array2)

elapsed_time_array = time.time() - start_time

print('Time', elapsed_time, elapsed_time_array)
