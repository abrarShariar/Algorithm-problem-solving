def mergeOverlappingIntervals(intervals):

    intervals.sort(key = lambda x: x[0])
    # sort the intervals by start date
    running_start = intervals[0][0]
    running_end = intervals[0][1]

    merged_list = []

    for i in range(1, len(intervals)):
        current_start = intervals[i][0]
        current_end = intervals[i][1]

        # the start time of the current interval inside the runnign intervcal's end => merge
        if current_start <= running_end:
            running_end = max(running_end, current_end)
        else:
            merged_list.append([running_start, running_end])

            running_start = current_start
            running_end = current_end

    merged_list.append([running_start, running_end])
    return merged_list


input_list = [[1,2], [3,5], [4,7], [6,8], [9,10]]
print(mergeOverlappingIntervals(input_list))