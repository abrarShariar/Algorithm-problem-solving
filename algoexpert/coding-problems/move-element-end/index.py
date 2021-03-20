# SOLVED
def moveElementToEnd(array, toMove):
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer < right_pointer:
        left_item = array[left_pointer]
        right_item = array[right_pointer]

        # if left_pointer => movable item and right pointer => nonto Move => swap
        if left_item == toMove and right_item != toMove:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
            left_pointer += 1
            right_pointer -= 1
        # the left_item is correct => move 
        if left_item != toMove:
            left_pointer += 1 
        # the right_item is correct => move
        if right_item == toMove:
            right_pointer -= 1

    return array


