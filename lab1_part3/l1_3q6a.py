def has_sum_naive(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == K:
                return True
    return False
arr = [8, 4, 1, 6]
K = 10
print("Has sum (O(n^2)):", has_sum_naive(arr, K))
