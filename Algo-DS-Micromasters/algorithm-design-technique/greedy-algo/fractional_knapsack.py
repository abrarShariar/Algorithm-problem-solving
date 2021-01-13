import sys

def get_optimal_value(capacity, weights, values):

	# O(n)
	per_unit_dict = {}
	# calculate the per unit
	for i in range(len(weights)):
		w, v = weights[i], values[i]
		per_unit = v/w
		per_unit_dict[i] = per_unit

	# O(nlogn)
	# sort the dict
	sorted_unit_dict = sorted(per_unit_dict.items(), key = lambda x: x[1], reverse = True)

	max_value = 0

	# O(n)
	for sorted_data in sorted_unit_dict:
		if capacity <= 0:
			return max_value

		sorted_index = sorted_data[0]
		sorted_per_unit = sorted_data[1]
		w = weights[sorted_index]
		v = values[sorted_index]

		# if w is within capacity
		if capacity >= w:
			capacity = capacity - w
			max_value += v
		elif capacity < w:
			max_value = max_value + (capacity * sorted_per_unit)
			capacity = 0
	
	return max_value


if __name__ == "__main__":
	print(get_optimal_value(10, [4, 3, 5], [10, 20, 30]))
	print(get_optimal_value(5, [4, 3, 5], [10, 20, 30]))

	data = list(map(int, sys.stdin.read().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]

	print(values)
	print(weights)

	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.10f}".format(opt_value))