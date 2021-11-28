# def remove_duplicates(arr):
# 	p1, p2  = 0, 1
# 	# p1 + 1 is the position we want to swap to 
# 	# p2 is the next pointer to check

# 	# [2,3,3,3,6,6,9,9]

# 	while p2 < len(arr):
# 		if arr[p1] != arr[p2]:
# 			p1 += 1
# 			p2 += 1
# 		else:
# 			# start a p' to find the next non-dup element and swap with p+1
# 			p_n = p2 + 1
# 			while p_n < len(arr) and arr[p_n] == arr[p2]:
# 				p_n += 1
			
# 			if p1 + 1 < len(arr) and p_n < len(arr):
# 				# swap with p+1
# 				arr[p1+1], arr[p_n] = arr[p_n], arr[p1+1]
# 				# increase p1 by 1, and p2 = p_n +1
# 				p1 = p1 + 1
# 				p2 = p_n + 1
# 			else:
# 				p1 += 1
# 				p2 += 1


# 	return p1+1

# print(remove_duplicates([2, 3, 3, 3, 6, 9]))
# print(remove_duplicates( [2, 3, 3, 3, 6,6,9,9] ))


# no need to swap 
def remove_duplicates(arr):
	p1, p2 = 0, 1

	while p1 < len(arr) and p2 < len(arr):
		if arr[p1] != arr[p2]:
			p1 += 1
			p2 += 1

		else:
			# if we found dups - move p2 till we find the non-dup element
			while p2 < len(arr) and arr[p1] == arr[p2]:
				p2 += 1
			
			# assign to the p1+1 spot
			if (p1 + 1) < len(arr) and p2 < len(arr):
				arr[p1+1] = arr[p2]
				p1 += 1
	
	return p1 + 1


print(remove_duplicates([2, 3, 3, 3, 6, 9]))
print(remove_duplicates([2, 3, 3, 3, 6,6,9, 9,10,20]))



