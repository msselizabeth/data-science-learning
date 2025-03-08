import numpy as np

# Challenge 1:
# Create a 2D array of shape (3, 4) (3 rows, 4 columns), filled with ones, in two different ways. Ensure their data types are the same and explicitly set the data type to float32.
a1 = np.ones((3, 4), dtype=np.float32)
a1_second = np.full((3, 4), 1, dtype=np.float32)  #

# print(a1)
# print(a1_second)


# Challenge 2:
# Create an array of ones of shape (6, 6) and index into it in such a way that the result is an array of shape (3, 4). The extracted sub-array should contain values from different positions of the original array, not just a single contiguous block.
a2 = np.ones((6, 6))
a2 = a2[0:3, 0:4]
# print(a2)


# Challenge 3:
# Create an empty array of shape (4, 4, 4) and iterate over its elements in two different ways:
# 1. Using a for loop.
# 2. Using a NumPy built-in function that allows iteration without explicit loops.
a3 = np.empty((4, 4, 4))
for a in a3:
    for i_a in a:
        for i in i_a:
            print(i)

for item in a3.flat:
    print(item)

# Challenge 4:
# Create an array of 200 elements from 0.05 to 10 named my_array, and change every 15th element to 500. The array values should be evenly spaced.
my_array = np.linspace(0.05, 10, 200)
my_array[::15] = 15
print(my_array)
