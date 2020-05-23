def merge_interval(intervals):
	if len(intervals) == 0:
		return None
	result = []
	# sort intervals
	intervals = sorted(intervals, key = lambda x : x[0])

	start = intervals[0][0]
	end = intervals[0][1]

	for i in range(1,len(intervals)):
		current_start = intervals[i][0]
		current_end = intervals[i][1]

		if current_start >= start and current_start <= end:
			start = min(current_start, start)
			end = max(current_end, end)
		else:
			result.append([start, end])
			start = current_start
			end = current_end

	result.append([start, end])
		
	return result

print(merge_interval([[1,3], [4,8], [5,10], [6, 11]]))
print(merge_interval([[1,4], [2,6], [3,5]]))
print(merge_interval([[6,7], [2,4], [5,9]]))
print(merge_interval([[1,100]]))
print(merge_interval([]))





