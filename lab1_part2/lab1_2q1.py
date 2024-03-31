import numpy as np
import time
import matplotlib.pyplot as plt

# Generate random numbers
random_numbers = np.random.randint(1, 10001, 1000)

# Define sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Measure time taken by each sorting algorithm
start_time = time.time()
bubble_sort(random_numbers.copy())
end_time = time.time()
bubble_time = end_time - start_time

start_time = time.time()
insertion_sort(random_numbers.copy())
end_time = time.time()
insertion_time = end_time - start_time

start_time = time.time()
selection_sort(random_numbers.copy())
end_time = time.time()
selection_time = end_time - start_time

start_time = time.time()
quick_sort(random_numbers.copy())
end_time = time.time()
quick_time = end_time - start_time

# Plot the time taken for each sorting algorithm
sorting_algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort']
times = [bubble_time, insertion_time, selection_time, quick_time]

plt.bar(sorting_algorithms, times, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken for Sorting Algorithms')
plt.show()
