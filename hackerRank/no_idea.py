n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

# convert arr to dict with count
dict = {}
for el in arr:
    dict[el] = dict.get(el, 0) + 1

# take A, B as input
A = list(map(int, input().split()))
B = list(map(int, input().split()))
h = 0
for i in range(len(A)):
    h += dict.get(A[i], 0)
    h += dict.get(B[i], 0) * -1

print(h)