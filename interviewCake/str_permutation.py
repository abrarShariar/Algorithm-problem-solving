# def get_perm(input_str):

#   # base case: return when there is only 1 char remaining
#   if len(input_str) <= 1:
#     # return a set of that 1 char
#     return set([input_str])

#   # contains the list of all chars except the last (abc => ab)
#   all_chars_except_last = input_str[:-1]

#   # the last char (abc => c)
#   last_char = input_str[-1]

#   # recursive call (keeps calling till the last index)
#   perm_all_chars_except_last = get_perm(all_chars_except_last)

#   # the result set
#   permutations_result = set()

#   # loop over all the permutations in the result list of recursive call
#   for ch in perm_all_chars_except_last:
#     # loop over each string elemtns 
#     for position in range(len(all_chars_except_last) + 1):
#       # different combination
#       item = (
#         ch[:position] + last_char + ch[position:]
#       )
#       # populate the permutation_result list
#       permutations_result.add(item)
  
#   # return result from each recursive call
#   return permutations_result
    
# print(get_perm('cat'))


def get_permutations(input_str):
	if len(input_str) <= 1:
		return set([input_str])

	all_chars_except_last = input_str[:-1]
	last_char = input_str[-1:]

	permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

	permutations = set()
	for perm_str in permutations_of_all_chars_except_last:
		for position in range(len(all_chars_except_last) + 1):
			item = (
				perm_str[:position] + last_char + perm_str[position:]
			)
			permutations.add(item)

	return permutations

	
print(get_permutations('cat'))






	
