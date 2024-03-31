def find_swapped_elements(arr):
    first_swap = None
    second_swap = None
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if first_swap is None:
                first_swap = i
            else:
                second_swap = i + 1
                break
    
    # If second_swap is still None, then the swapped elements are adjacent
    if second_swap is None:
        second_swap = first_swap + 1
    
    return first_swap, second_swap

def sort_array(arr):
    first_swap, second_swap = find_swapped_elements(arr)
    
    # Swap the elements to restore sorted order
    arr[first_swap], arr[second_swap] = arr[second_swap], arr[first_swap]
    
    return arr

arr = [3, 8, 6, 7, 5, 9]
sorted_arr = sort_array(arr)
print("Sorted array:", sorted_arr)
