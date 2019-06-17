import math
n, m, a = list(input().strip().split(" "))
print(math.ceil(int(n)/int(a)) * math.ceil(int(m)/int(a)))
