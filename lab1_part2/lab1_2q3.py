import heapq

def find_k_largest_elements(arr, k):
    # Create a min-heap of size k to store the k largest elements
    heap = arr[:k]
    heapq.heapify(heap)  # Convert the list into a min-heap
    
    # Traverse the remaining elements in the array
    for num in arr[k:]:
        # If the current element is greater than the smallest element in the heap
        if num > heap[0]:
            heapq.heappop(heap)  # Remove the smallest element from the heap
            heapq.heappush(heap, num)  # Push the current element onto the heap
    
    # Return the k largest elements from the heap
    return heap

# Example usage:
arr = [3, 1, 8, 5, 7, 2, 9, 4, 6]
k = 3
print(find_k_largest_elements(arr, k))
