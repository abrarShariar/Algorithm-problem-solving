def isMonotonic(array):
    if len(array) <= 2:
        return True
    # determine the order
    isIncreasing = 0
    if array[0] <= array[1]:
        isIncreasing = 1

    for i in range(len(array) - 1):
        if isIncreasing and abs(array[i]) > abs(array[i+1]):
            return False
        elif not isIncreasing and abs(array[i]) < abs(array[i+1]):
            return False

    return True