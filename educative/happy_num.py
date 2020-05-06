def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square_sum(slow)  # move one step
    fast = find_square_sum(find_square_sum(fast))  # move two steps
    if slow == fast:  # found the cycle
      break
  return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
  _sum = 0
  while (num > 0):
    digit = num % 10
    _sum += digit * digit
    num //= 10
  return _sum


# def find_happy_number(num):
# 	dict = {}
# 	while num != 1:
# 		# split the num by digits
# 		num_list = [int(i)**2 for i in str(num)]
# 		num = sum(num_list)
# 		dict[num] = dict.get(num, 0) + 1
# 		if dict[num] > 1:
# 			# found a cycle
# 			return False

# 	return True


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))

main()