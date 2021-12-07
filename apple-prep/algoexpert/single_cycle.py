# SOLVED!
def hasSingleCycle(array):
    # store the index - and the number of times visited
    visited_index_counts = {}
    current_index = 0
    start_index = current_index
    upper_bound = len(array) - 1
    lower_bound = 0

    while True:
        if len(visited_index_counts.keys()) == len(array):
            if current_index != start_index:
                return False
            else:
                return True

        if current_index in visited_index_counts.keys():
            # we are visiting this index twice
            return False

        visited_index_counts[current_index] = 1
        next_index = current_index + array[current_index]
        # wrap around - from both sides of course
        while next_index > upper_bound or next_index < lower_bound:
            if next_index > upper_bound:
                next_index = next_index - upper_bound
                next_index = (lower_bound + next_index) - 1
            elif next_index < lower_bound:
                next_index = (upper_bound + next_index) + 1

        current_index = next_index

    return True

# print(hasSingleCycle([2,3,1,-4,-4,2]))
print(hasSingleCycle([1, 1, 1, 1, 2]))

