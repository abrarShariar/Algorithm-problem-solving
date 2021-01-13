import math
INFINITY = math.inf

# O(n^2) solution => not optimal
def minToTotalWaitingTime(time_list, total_patient):
	#	the total waiting time we return
	waiting_time = 0

	# total number of patients who have been already treated
	treated = [0 for i in range(total_patient)]

	# loop over all patient waiting time
	for i in range(total_patient):
		t_min = INFINITY
		min_index = 0

		for j in range(total_patient):
			if treated[j] == 0 and time_list[j] < t_min:
				t_min = time_list[j]
				min_index = j
		
		treated[min_index] = 1
		waiting_time = waiting_time + ((total_patient - (i+1)) * t_min)

	return waiting_time

# optimal
# O(nlogn)
def minToTotalWaitingTime_optimal(time_list, total_patient):
	waiting_time = 0

	# sort the time_list
	time_list.sort()

	for i in range(0, len(time_list) - 1):
		waiting_time = waiting_time + (total_patient - (i+1))*time_list[i] 
	
	return waiting_time

print(minToTotalWaitingTime_optimal([4,100,10], 3))

