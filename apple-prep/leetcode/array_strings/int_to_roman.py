# SOLVED!
class Solution:
	def intToRoman(self, num: int) -> str:
		roman_value_map = {
			1: 'I',
			5: 'V',
			10: 'X',
			50: 'L',
			100: 'C',
			500: 'D',
			1000: 'M',
			4: 'IV',
			9: 'IX',
			40: 'XL',
			90: 'XC',
			400: 'CD',
			900: 'CM'
		};

		running_num = num
		running_roman_num = ''
		res_roman = ""
		sorted_num_list = sorted(roman_value_map.keys())

		lower_bound = sorted_num_list[0]
		upper_bound = sorted_num_list[len(sorted_num_list) - 1]

		while running_num > 0:
			current_num = 0
			# find the corresponding value in roman_value_map
			if running_num >= upper_bound:
				current_num = upper_bound
			elif running_num <= lower_bound:
				current_num = lower_bound
			else:		
				for i in range(1, len(sorted_num_list)):
					if running_num == sorted_num_list[i]:
						current_num = sorted_num_list[i]
						break
					elif running_num < sorted_num_list[i]:
						current_num = sorted_num_list[i-1]
						break
			
			running_roman_char = roman_value_map[current_num]
			# update the result roman value
			res_roman += running_roman_char
			running_num = running_num - current_num

		return res_roman

sol = Solution()
# print(sol.intToRoman(1994))
# print(sol.intToRoman(1))
# print(sol.intToRoman(58))
# print(sol.intToRoman(9))
# print(sol.intToRoman(3))
print(sol.intToRoman(400))