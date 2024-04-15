def maximize_index_product(arr):
    """Rearranges the array to maximize the sum of arr[i] * i using a Greedy approach."""
    # Sort the array to maximize the product sum
    arr.sort()
    max_sum = 0
    for i in range(len(arr)):
        max_sum += arr[i] * i
    return max_sum

arr = [2, 5, 3, 4, 0]
maximize_index_product(arr)