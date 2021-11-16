def test_ref(name):
	name = 'Minato-ku'
	print(name)

input_name = "Shibuya-ku"
test_ref(input_name)
print(input_name)

def test_my_array(input_array):
	
	print("Priting all the elements:")
	for element in input_array:
		print(element)

	print("Total number of elements: ", len(input_array))
	input_array[1] = 999999

	print()


input_list = [1,2,3,4,5,6,7,8,9,10]
# the input list gets passed by reference
test_my_array(input_list)

print(input_list)

