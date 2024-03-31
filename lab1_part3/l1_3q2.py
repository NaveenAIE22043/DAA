def max_product_pair(arr):
    if len(arr) < 2:
        return None, None
    
    max_product = float('-inf')
    pair = None
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                pair = (arr[i], arr[j])
    
    return pair, max_product

arr = [1, 7, 4, 2, 8, 6, 3, 9, 5]
result_pair, product = max_product_pair(arr)
if result_pair:
    print("Pair with maximum product:", result_pair)
    print("Product of the pair:", product)
else:
    print("No pair found.")
