def lonely_number(numbers):
  # fill in
  n = numbers[0]
  for i in range(1, len(numbers)):
    n = n ^ numbers[i]
  return n

print(lonely_number([4,1,4,7,9,7,1]))