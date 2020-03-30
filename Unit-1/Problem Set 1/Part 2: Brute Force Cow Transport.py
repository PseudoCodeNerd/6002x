# Problem 2

from ps1_partition import get_partitions


def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """


    '''
    Idea 1
    use get_partitions to generate all possible combinations, then filter out combinations
    where weight of cows exceeds the limit (+ where all cows are present), then return list
    of minimum length.
    Simple, inefficient.
    
    Idea 2 
    use dfs to iterate through all nodes and find one with minimum trips, remove same with set
    Complex(?), highly efficient
    '''
    # Idea 1
    possible_combinations = []
    for partition in get_partitions(cows.keys()):
        possible_combinations.append(partition)
    possible_combinations.sort(key=len)

    valid_combinations = possible_combinations.copy()

    for partition in possible_combinations:
        for trip in partition:
            total = sum([cows.get(cow) for cow in trip])
            if total > limit:
                valid_combinations.remove(partition)
                break

    return min(valid_combinations, key=len)

    # Idea 2


print(brute_force_cow_transport({'Louis': 45, 'Patches': 60, 'Polaris': 20, 'Milkshake': 75, 'Muscles': 65, 'Clover': 5,
                                 'Horns': 50, 'MooMoo': 85, 'Miss Bella': 15, 'Lotus': 10}, 100))
