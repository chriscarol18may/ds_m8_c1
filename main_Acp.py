import numpy as np

# 1. Create an array consisting of linearly spaced elements between 0 to 9
# (np.arange(10) produces [0, 1, 2, ..., 9]; np.linspace(0, 9, 10) also works)
arr = np.arange(10)
print("1. Original Array:\n", arr)

# 2. Replace all odd numbers in this array with -1 without modifying the original array
modified_arr = np.where(arr % 2 != 0, -1, arr)
print("\n2. Array with odd numbers replaced by -1:\n", modified_arr)
print("   Original array remains unchanged:\n", arr)

# 3. Convert the original 1D array into a 2D array with two rows
arr_2d = arr.reshape(2, -1)  # shape (2, 5)
print("\n3. Reshaped 2D Array (2 rows):\n", arr_2d)

# 4. Iterate through the original array and find the sum of all evens
even_sum = 0
for num in arr:
    if num % 2 == 0:
        even_sum += num

print("\n4. Sum of all even numbers:", even_sum)