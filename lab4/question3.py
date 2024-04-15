def minimize_sum_product(array_one, array_two):
    """Rearranges two arrays such that the sum of products of their elements is minimized."""
    # Sort both arrays, one in ascending and the other in descending to minimize the product sum
    array_one.sort()
    array_two.sort(reverse=True)
    min_sum = sum(a * b for a, b in zip(array_one, array_two))
    return min_sum

array_one = [7, 5, 1, 4]
array_two = [6, 17, 9, 3]
minimize_sum_product(array_one, array_two)