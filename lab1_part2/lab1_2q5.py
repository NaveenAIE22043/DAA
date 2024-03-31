def merge_intervals(intervals):
    # Sort intervals based on start times
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = []
    
    for interval in intervals:
        # If merged_intervals is empty or the current interval does not overlap with the last merged interval
        if not merged_intervals or interval[0] > merged_intervals[-1][1]:
            merged_intervals.append(interval)
        else:
            # Update the end time of the last merged interval if necessary
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
    
    return merged_intervals

# Example usage:
intervals = [(1, 4), (2, 5), (7, 8), (6, 9)]
non_overlapping_intervals = merge_intervals(intervals)
print("Non-overlapping intervals after merging:")
for interval in non_overlapping_intervals:
    print(interval)
