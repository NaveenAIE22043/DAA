import heapq

def merge_sorted_lists(arrays):
    # Initialize an empty list to store the merged result
    merged_list = []
    
    # Initialize a min-heap to efficiently merge the lists
    heap = []
    
    # Add the first element of each list to the min-heap
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))  # (element, list index, index in list)
    
    # Merge the lists until the min-heap is empty
    while heap:
        val, arr_idx, idx_in_arr = heapq.heappop(heap)
        merged_list.append(val)  # Append the minimum value to the merged list
        
        # If there are more elements in the same list, push the next element to the min-heap
        if idx_in_arr + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][idx_in_arr + 1]
            heapq.heappush(heap, (next_val, arr_idx, idx_in_arr + 1))
    
    return merged_list

# Example usage:
arrays = [[10,20, 30,40], [15, 25, 35], [27,29,37,48,93],[32,33]]
print(merge_sorted_lists(arrays))
