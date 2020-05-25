# sample I/O
# [[1,3], [5,7], [8,12]], [4,6]
# [[1,3], [4,7], [8,12]]

# [[1,3], [5,7], [8,12]]
# [4,10]
# [[1,3], [4,12]]

# [[2,3],[5,7]]
# [1,4]
# [[1,4], [5,7]]

def insert_interval(intervals, new_interval):
	i, START, END = 0, 0, 1
	result = []

	# loop over all intervals whose end date is before the new_interval's end date
	while i < len(intervals) and intervals[i][END] < new_interval[START]:
		result.append(intervals[i])
		i += 1
	
	# loop over and merge
	while i < len(intervals) and intervals[i][START] <= new_interval[END]:
		new_interval[START] = min(intervals[i][START], new_interval[START])
		new_interval[END] = max(intervals[i][END], new_interval[END])
		i += 1

	# insert the merged interval
	result.append([new_interval[START], new_interval[END]])

	# insert any remaining intervals
	while i < len(intervals):
		result.append(intervals[i])
		i += 1

	return result

print(insert_interval([[1,3], [5,7], [8,12]], [4,6]))
print(insert_interval([[1,3], [5,7], [8,12]], [4,10]))
print(insert_interval([[2,3],[5,7]], [1,4]))
print(insert_interval([[2,3],[5,7]], [100,400]))
print(insert_interval([[2,3],[5,7]], [1,400]))