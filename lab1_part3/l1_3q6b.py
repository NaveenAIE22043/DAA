def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def has_sum_sorted(arr, K):
    arr.sort()
    for num in arr:
        complement = K - num
        if binary_search(arr, complement):
            return True
    return False

# Example usage:
arr = [8, 4, 1, 6]
K = 10
print("Has sum (O(n*log(n))):", has_sum_sorted(arr, K))
