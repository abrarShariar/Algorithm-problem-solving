def celebration_party(age_list):
	# sort
	age_list.sort()

	# greedy segments
	segments = []
	left = 0

	while left < len(age_list):
		(left_most_age, right_most_age) = (age_list[left], age_list[left] + 2)
		segments.append((left_most_age, right_most_age))

		while left < len(age_list) and age_list[left] <= right_most_age:
			left += 1

	return segments

print(celebration_party([2,3,4,5,6,7,8,9]))
print(celebration_party([2,3,4,10,5,12,45]))