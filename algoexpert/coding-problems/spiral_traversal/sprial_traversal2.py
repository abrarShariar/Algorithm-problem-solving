def spiralTraverse(array):
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1

    result_list = []

    while start_col <= end_col and start_row <= end_row:
        # top left to right
        current_col = start_col
        while current_col <= end_col:
            result_list.append(array[start_row][current_col])
            current_col += 1

        # top to bottom
        current_row = start_row + 1
        while current_row <= end_row:
            result_list.append(array[current_row][end_col])
            current_row += 1
        
        # bottom right to left
        current_col = end_col - 1
        while current_col >= start_col:
            result_list.append(array[end_row][current_col])
            current_col -= 1

        # bottom to top
        current_row = end_row - 1
        while current_row > start_row:
            result_list.append(array[current_row][start_col])
            current_row -= 1

        start_row += 1
        start_col += 1
        end_col -= 1
        end_row -= 1

    return result_list



input_array = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(spiralTraverse(input_array))