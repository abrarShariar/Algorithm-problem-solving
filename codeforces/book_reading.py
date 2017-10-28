# input
n,t = map(int,raw_input().split())


seconds_in_each_day = 86400

a = raw_input().split()
    
# calculation
reading_day_counter = 0
reading_time_each_day = 0
for index in range(0,n):
    temp = seconds_in_each_day - int(a[index])
    reading_time_each_day += temp
    reading_day_counter += 1
    if reading_time_each_day >= t:
        break
    
# print output
print reading_day_counter

# ACCEPTED