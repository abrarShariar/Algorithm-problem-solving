# SOLVED
def kadanesAlgorithm(array):
    # Write your code here.
    current_max = array[0]
    global_max = current_max

    for i in range(1, len(array)):
        current_max = max(array[i], current_max + array[i])
        global_max = max(current_max, global_max)

    return global_max


print(kadanesAlgorithm([-2,3,2,1]))
print(kadanesAlgorithm([1,-2,3,4]))