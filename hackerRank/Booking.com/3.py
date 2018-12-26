
def howManyAgentsToAdd(noOfCurrentAgents, callsTime):
    if len(callsTime) == 1:
        return 0
    new_array = []
    for i in range(len(callsTime)):
        new_array.append((callsTime[i][0], callsTime[i][1]))

    # sort based on first key
    sorted_array = sorted(new_array, key = lambda x: x[0])
    # print(sorted_array)
    agents = 0
    for i in range(1, len(sorted_array)):
        start = sorted_array[i][0]
        end = sorted_array[i][1]

        if start <= sorted_array[i-1][1]:
            agents += 1

    # print(agents)
    if agents == 0:
        return agents
    else:
        if agents > noOfCurrentAgents:
            return agents - noOfCurrentAgents
        return 0



def main():
    noOfCurrentAgents = int(input().strip())

    callsTimes_rows = int(input().strip())
    callsTimes_columns = int(input().strip())

    callsTimes = []

    for _ in range(callsTimes_rows):
        callsTimes.append(list(map(int, input().rstrip().split())))

    # print(callsTimes)

    res = howManyAgentsToAdd(noOfCurrentAgents, callsTimes)
    print(res)

main()
