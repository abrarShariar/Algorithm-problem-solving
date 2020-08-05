# SOLVED
import functools

def sum_digits(num):
		# initialize the sum
		sum = 0

		while int(num/10) > 0:
			# break current number into digits
			current_num = num
			
			temp_sum = 0
			while current_num > 0:
				rem = current_num % 10
				current_num = int(current_num / 10)
				temp_sum += rem
			
			sum += temp_sum
			num = temp_sum

		return num

			
print(sum_digits(49))
print(sum_digits(199))