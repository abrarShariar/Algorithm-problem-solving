def spiralTraverse(array):
    start_row, start_col = 0, 0
    end_row, end_col = 3, 3
    
    while True:
        current_row = start_row
        current_col = start_col

        # left to right
        while current_col < end_col:
            print(array[current_row], array[current_col])
            current_col += 1

        current_col = end_col
        # top to down
        while current_row < end_row:
            print(array[current_row], array[current_col])
            current_row += 1
        
        current_row = end_row
        # right to left 
        while current_col > start_col:
            print(array[current_row], array[current_col])
            current_col -= 1

        current_col = start_col
        # down to top
        while current_row > start_row:
            print(array[current_row], array[current_col])
            current_row -= 1

        # reset the start and end indices
        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1
        
        if start_row == start_col:
            break

spiral_traversal(array)