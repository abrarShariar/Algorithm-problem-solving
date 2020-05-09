# price list = [lowest, higest, average, count]

def main():
	# take input
	N = int(input())
	for i in range(N):
		t = int(input("\n"))
		dict = {}
		for j in range(t):
			line = input().split(" ")
			fruit_name = line[0]
			price = int(line[1])
			# check if fruit is already in dict
			if fruit_name in dict.keys():
				# increase count
				dict[fruit_name][3] += 1
				# set min max
				if price <= dict[fruit_name][0]:
					dict[fruit_name][0] = price
				elif price > dict[fruit_name][1]:
					dict[fruit_name][1] = price
				# calculate average
				dict[fruit_name][2] = (dict[fruit_name][2] + price) // dict[fruit_name][3]
			else:
				dict[fruit_name] = [price, price, price, 1]
		
		# show output
		print("Case #", i+1)
		for key in sorted(dict.keys()):
			print(key, dict[key][0], dict[key][1], dict[key][2])


main()