# SOLVED
class Solution:
	def myAtoi(self, s: str) -> int:
		res_str = s.strip()
		digit_lower_limit = ord('0')
		digit_upper_limit = ord('9')
		sign_char = ''
		
		if res_str == "":
			return 0
		elif res_str[0] != "+" and res_str[0] != "-":
			# return 0 - if the string is nothing but whitespace and the first char is not wihin the number raneg
			if not (ord(res_str[0]) >= ord('0') and ord(res_str[0]) <= ord('9')):
				return 0
		else:
			sign_char = res_str[0]

		lower_limit = (-2)**31
		upper_limit = (2)**31 - 1

		new_res_str = ""
		# start looping over and create the number
		for i in range(len(res_str)):
			ch = res_str[i]
			# if it's a sign 
			if (ch == "+" or ch == "-"):
				if i != 0:
					break
				else:
					new_res_str += ch
			# if it's not a digit sign - break free
			elif not (ord(ch) >= digit_lower_limit and ord(ch) <= digit_upper_limit):
				break
			else:
				new_res_str += ch
		
		if (new_res_str[0] == '+' or new_res_str[0] == '-') and len(new_res_str) == 1:
			return 0

		# clamp the shit out
		res_int = int(new_res_str)
		
		if res_int <= lower_limit:
			return lower_limit
		elif res_int >= upper_limit:
			return upper_limit

		return res_int

		
# sol = Solution()
# print(sol.myAtoi('-12313'))
# print(sol.myAtoi('    12313'))
# print(sol.myAtoi('+12313'))
# print(sol.myAtoi('words have meaning 12313'))
# print(sol.myAtoi('123123123 words'))