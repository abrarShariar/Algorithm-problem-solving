# SOLVED O(N)
def insert_interval(intervals, new_interval):
	if len(intervals) == 0 or len(new_interval) == 0:
		return []

	intervals = sorted(intervals, key = lambda x: x[0])
	result = []
	START = 0
	END = 1

	start_val = intervals[0][START]
	end_val = intervals[0][END]

	i = 0
	while i < len(intervals):
		current_start = intervals[i][START]
		current_end = intervals[i][END]
		j = i
		i += 1
		while j < len(intervals) and intervals[j][START] >= new_interval[START] and intervals[j][START] <= new_interval[END]:
			new_interval[START] = min(new_interval[START], intervals[j][START])
			new_interval[END] = max(new_interval[END], intervals[j][END])
			current_start = new_interval[START]
			current_end = new_interval[END]
			j += 1
			i = j
		
		result.append([current_start, current_end])
	
	return result

print(insert_interval([[1,3], [5,7], [8,12]], [4,6]))
print(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10]))
print(insert_interval([[2, 3], [5, 7]], [1, 4]))
print