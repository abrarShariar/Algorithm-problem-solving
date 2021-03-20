# DONE
def smallestDifference(arrayOne, arrayTwo):
    # sort the two arrays
    arrayOne.sort()
    arrayTwo.sort()
    result_box = []
    # initialize the pointers
    px, py = 0, 0
    min_diff = abs(arrayOne[px] - arrayTwo[py])
    while px < len(arrayOne) and py < len(arrayTwo):
        x_item = arrayOne[px]
        y_item = arrayTwo[py]

        if abs(x_item - y_item) <= min_diff:
            result_box = [x_item, y_item]
            min_diff = abs(x_item - y_item)

        # move the item smaller to be closer to the larger one
        if x_item < y_item:
            px += 1
        elif y_item < x_item:
            py += 1
        else:
            return [x_item, y_item]

    return result_box
        
print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))