def zigzag_traversal(input_list):
	result_list = []
	root = input_list[0]
	result_list.append([root])
	is_left_to_right = 0

	left_node_pointer = 1
	right_node_pointer = 2

	# loop over all the nodes in zigzag
	while right_node_pointer < len(input_list):
		left_node = input_list[left_node_pointer]
		right_node = input_list[right_node_pointer]

		if not (left_node == None and right_node == None):
			if is_left_to_right == 1:
				result_list.append([left_node, right_node])
				is_left_to_right = 0
			else:
				result_list.append([right_node, left_node])
				is_left_to_right = 1

		left_node_pointer += 2
		right_node_pointer += 2

	return result_list

print(zigzag_traversal([3,9,20,None,None,15,7, 1, 2, 4, 5, 6, 7, 8, 9]))
# print(zigzag_traversal([3,9,20]))
# print(zigzag_traversal([3,9,20, None, None]))



		


