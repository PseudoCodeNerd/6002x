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
# Test Cases


print(greedy_cow_transport({'Louis': 45, 'Patches': 60, 'Polaris': 20, 'Milkshake': 75, 'Muscles': 65, 'Clover': 5,
                            'Horns': 50, 'MooMoo': 85, 'Miss Bella': 15, 'Lotus': 10}, 100))
print(greedy_cow_transport({'Daisy': 50, 'Coco': 10, 'Rose': 50, 'Willow': 35, 'Betsy': 65, 'Dottie': 85, 'Abby': 38,
                            'Lilly': 24, 'Patches': 12, 'Buttercup': 72}, 100))
print(greedy_cow_transport({'Coco': 59, 'Rose': 42, 'Willow': 59, 'Betsy': 39, 'Abby': 28, 'Starlight': 54, 'Luna': 41,
                            'Buttercup': 11}, 120))
