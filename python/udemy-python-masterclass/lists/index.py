# my_list = [x**2 for x in range(1,11)]
# new_list = [x**2 for x in range(1, 11) if x > 5]
# print(new_list)

# a = lambda x, y: x * y
# print(a(2, 20))

def my_num(x):
   return x**2

result = map(lambda x: x ** 2, [1,2,3,4,5])
print(list(result))

filtered_list = filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8])
print(list(filtered_list))