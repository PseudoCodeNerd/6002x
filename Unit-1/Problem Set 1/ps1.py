###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Enter your code for the Greedy Cow Transport here
# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # making a list of lists of cows and weights in descending order of weight using insertion sort
    # cow list : [['MooMoo', 85], ['Milkshake', 75], ['Muscles', 65], ['Patches', 60], ['Horns', 50], ['Louis', 45],
    # ['Polaris', 20], ['Miss Bella', 15], ['Lotus', 10], ['Clover', 5]]
    cow_list = [[k, v] for k, v in cows.items()]
    for i in range(len(cow_list)):
        temp = cow_list[i]
        j = i - 1
        while j >= 0 and temp[1] > cow_list[j][1]:
            cow_list[j + 1] = cow_list[j]
            j -= 1
        cow_list[j + 1] = temp
    trips = []
    while True:
        curr_trip, total_weight = [], 0
        for i in cow_list:
            if total_weight + i[1] <= limit:
                # cow list has elements as [['MooMoo', 85], [cow_name, cow_weight], ...]
                curr_trip.append(i[0])
                # curr_trip contains eligible cow names in a list.
                total_weight += i[1]
        trips.append(curr_trip)  # trips now looks something like this : [ [cow_name, cow_name] ]
        temp = []
        for i in cow_list:
            if i[0] not in curr_trip:
                temp.append(i)
        cow_list = temp
        if not cow_list:
            break
    return trips

# correct! 20/20

# Problem 2


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
    # TODO: Your code here

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

    # correct 20/20
        
# Problem 3


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit = 10
# print(cows)

# start = time.time()
print(greedy_cow_transport(cows, limit))  # 2.47955322265625e-05 s
# end = time.time()
# print(end - start)

# start = time.time()
print(brute_force_cow_transport(cows, limit))  # 2.752690315246582s (oof so inefficient, perhaps dp should be used)
# end = time.time()
# print(end - start)

'''
1. Now that you have run your benchmarks, which algorithm runs faster?

[x] The Greedy Transport Algorithm
    The Brute Force Transport Algorithm
    They take the same amount of time
    
2. Consider the properties of the GREEDY algorithm. Will it return the optimal solution?

    Yes, all the time
    No, never
[x] It could, but it depends on the data, not always.

3. Consider the properties of the BRUTE FORCE algorithm. Will it return the optimal solution?

[x] Yes, all the time
    No, never
    It could, but it depends on the data, not always.
'''

# 26/26
# Fin. PSET1
