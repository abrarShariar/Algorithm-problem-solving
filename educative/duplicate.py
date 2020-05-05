def remove_duplicates(arr):
	i = 0
	j = i + 1
	c = 1
	while j < len(arr):
		if arr[i] != arr[j]:
			i = j
			c += 1
		j += 1			

	return c

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))	
print(remove_duplicates([2, 2, 2, 11]))