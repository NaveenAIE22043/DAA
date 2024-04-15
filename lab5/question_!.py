def candies(n, ratings):
    candies = [1] * n  # Start with giving each child at least one candy

    # First pass: scan from left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Second pass: scan from right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

# Example usage:
ratings = [4, 6, 4, 5, 6, 2]
print(candies(len(ratings), ratings))