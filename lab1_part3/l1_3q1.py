
def find_all_pairs_with_sum(arr, target_sum):
    # Create an empty dictionary to store elements and their indices
    num_index_map = {}
    pairs = []

    # Iterate through the array
    for num in arr:
        # Calculate the complement required to achieve the target sum
        complement = target_sum - num
        
        # If the complement is present in the dictionary, a pair is found
        if complement in num_index_map:
            # Add the pair to the list of pairs
            pairs.append([num, complement])
        
        # Store the current element in the dictionary
        num_index_map[num] = True

    return pairs

# Example usage:
arr = [8, 7, 2, 5, 3, 1]
target_sum = 10 
pairs = find_all_pairs_with_sum(arr, target_sum)
if pairs:
    print("Pairs found with the given sum:")
    for pair in pairs:
        print(pair)
else:
    print("No pairs found with the given sum.")