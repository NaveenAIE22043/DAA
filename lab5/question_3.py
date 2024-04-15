def pylons(k, arr):
    n = len(arr)
    last_plant = -1
    plants_count = 0
    i = 0

    while i < n:
        # Find the furthest city to place a power plant
        plant_pos = min(i + k - 1, n - 1)
        while plant_pos > last_plant and (arr[plant_pos] == 0 or plant_pos >= i + k):
            plant_pos -= 1
        if plant_pos == last_plant:  # no valid place found
            return -1
        last_plant = plant_pos
        plants_count += 1
        i = plant_pos + k  # move to the city beyond the current plant's range

    return plants_count

cities = [0, 1, 1, 1, 1, 0]
range_k = 2
print(pylons(range_k, cities))