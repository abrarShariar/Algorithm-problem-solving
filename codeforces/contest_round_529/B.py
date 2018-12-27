n = int(input())
a = input().strip().split(' ')
a = list(map(lambda x: int(x), a))

cur_max = max(a)
cur_min = min(a)
# instability = cur_max - cur_min

# remove cur_max from a then check
new_arr_max = a[:]
new_arr_max.remove(cur_max)
new_instability_max = max(new_arr_max) - min(new_arr_max)

# remove cur_min from a then check
new_arr_min = a[:]
new_arr_min.remove(cur_min)
new_instability_min = max(new_arr_min) - min(new_arr_min)

if new_instability_max < new_instability_min:
    print(new_instability_max)
else:
    print(new_instability_min)
