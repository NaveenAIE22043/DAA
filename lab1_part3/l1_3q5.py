def merge_and_count_inversions(arr, left, mid, right):
    left_subarray = arr[left:mid+1]
    right_subarray = arr[mid+1:right+1]

    i = j = k = inversion_count = 0

    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[left+k] = left_subarray[i]
            i += 1
        else:
            arr[left+k] = right_subarray[j]
            j += 1
            inversion_count += (mid + 1) - (left + i)
        k += 1

    while i < len(left_subarray):
        arr[left+k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        arr[left+k] = right_subarray[j]
        j += 1
        k += 1

    return inversion_count

def merge_sort_and_count_inversions(arr, left, right):
    inversion_count = 0
    if left < right:
        mid = (left + right) // 2
        inversion_count += merge_sort_and_count_inversions(arr, left, mid)
        inversion_count += merge_sort_and_count_inversions(arr, mid+1, right)
        inversion_count += merge_and_count_inversions(arr, left, mid, right)
    return inversion_count

def inversion_count(arr):
    return merge_sort_and_count_inversions(arr, 0, len(arr)-1)

# Example usage:
A = [10, 1, 2, 4, 13, 9, 5]
print("The number of inversions:", inversion_count(A))
