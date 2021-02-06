# SOLVED
def minimumWaitingTime(queries):
    queries.sort()
    waiting_time = 0
    running_sum = 0

    for i in range(len(queries) - 1):
        waiting_time += queries[i]
        running_sum += waiting_time

    return running_sum
