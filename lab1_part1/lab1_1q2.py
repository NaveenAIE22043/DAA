import numpy as np
import time
import matplotlib.pyplot as plt

# Generate random array
array = np.random.randint(1, 1001, 10000)
array.sort()  # Binary search requires a sorted array

# Linear search function
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary search function
def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Perform searches and measure time
search_times_linear = []
search_times_binary = []

for _ in range(5):
    search_key = int(input("Enter the search key: "))
    
    start_time = time.time()
    linear_search(array, search_key)2
    search_times_linear.append(time.time() - start_time)
    
    start_time = time.time()
    binary_search(array, search_key)
    search_times_binary.append(time.time() - start_time)

# Plotting
search_indices = range(1, 6)

plt.plot(search_indices, search_times_linear, label='Linear Search')
plt.plot(search_indices, search_times_binary, label='Binary Search')
plt.xlabel('Search Iteration')
plt.ylabel('Time (seconds)')
plt.title('Time taken for Linear and Binary Searches')
plt.legend()
plt.show()
