def max_activities(activities):
    # Sort activities by their finishing time
    activities.sort(key=lambda x: x[1])
    
    # Initialize variables
    max_activities_count = 0
    prev_finish_time = float('-inf')
    selected_activities = []
    
    # Iterate through the sorted activities
    for activity in activities:
        start_time, finish_time = activity
        
        # If the current activity can be performed after the previous one finishes, select it
        if start_time >= prev_finish_time:
            max_activities_count += 1
            prev_finish_time = finish_time
            selected_activities.append(activity)
    
    return max_activities_count, selected_activities

# Example usage:
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
max_count, selected_activities = max_activities(activities)

print("Maximum number of activities performed by a single person:", max_count)
print("Selected activities:")
for activity in selected_activities:
    print(activity)
