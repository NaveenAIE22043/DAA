def maximumPeople(pops, towns, clouds, ranges):
    from collections import defaultdict

    # Map each town to its population and whether it is covered by clouds
    covered = defaultdict(int)
    town_pop = dict(zip(towns, pops))
    
    # Mark range of clouds coverage
    for cloud_center, cloud_range in zip(clouds, ranges):
        for town in towns:
            if abs(town - cloud_center) <= cloud_range:
                covered[town] += 1

    # Removing one cloud
    max_sunny_pop = 0
    for i, (cloud_center, cloud_range) in enumerate(zip(clouds, ranges)):
        # Recalculate sunny population when removing each cloud
        temp_covered = covered.copy()
        for town in towns:
            if abs(town - cloud_center) <= cloud_range:
                temp_covered[town] -= 1
        sunny_pop = sum(pop for town, pop in town_pop.items() if temp_covered[town] == 0)
        max_sunny_pop = max(max_sunny_pop, sunny_pop)
    
    return max_sunny_pop


pops = [10, 100]
towns = [5, 100]
clouds = [4]
ranges = [1]
print(maximumPeople(pops, towns, clouds, ranges))