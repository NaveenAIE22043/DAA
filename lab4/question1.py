def fractional_knapsack(value_weight, capacity):
    """Solves the fractional knapsack problem given a list of (value, weight) tuples and total capacity.
    Returns the maximum value achievable within the given capacity."""
    # Sorting items by value to weight ratio in descending order
    value_weight.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    total_value = 0  # Total value accumulated
    for value, weight in value_weight:
        if capacity > 0 and weight <= capacity:
            # We can take full item
            capacity -= weight
            total_value += value
        else:
            # Take fraction of the remaining item
            total_value += value * (capacity / weight)
            break
    return total_value

items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
fractional_knapsack(items, capacity)