def find_string_anagrams(str, pattern):
    # create the pattern dict
    result_list = []
    pattern_dict = {}
    for ch in pattern:
        pattern_dict[ch] = pattern_dict.get(ch, 0) + 1
    
    window_start = 0
    matched = 0

    for window_end in range(len(str)):
        left_char = str[window_start]
        right_char = str[window_end]
        
        # at any point if the matched count is equal to the length of the pattern dict => we found a match
        if matched == len(pattern_dict):
            result_list.append(window_start) 

        if window_end >= len(pattern):
            # shrink the window
            # if the outgoing char is in the pattern dict => remove that
            if left_char in pattern_dict:
                pattern_dict[left_char] += 1
                if pattern_dict[left_char] > 0:
                    matched -= 1
            
            window_start += 1

        # if the right_char exists in the 
        if right_char in pattern_dict:
            pattern_dict[right_char] -= 1

            # if the pattern_dict is zero we have all the necessary matched chars
            if pattern_dict[right_char] == 0:
                matched += 1

    result_list.append(window_start)
    return result_list
        

# def find_string_anagrams(str, pattern):
#     result_indexes = []
#     pattern_dict = {}

#     # create the pattern dictionary
#     for ch in pattern:
#         pattern_dict[ch] = pattern_dict.get(ch, 0) + 1
    
#     window_start = 0
#     matched = 0

#     # slide the window till end
#     for window_end in range(len(str)):
#         left_char = str[window_start]
#         right_char = str[window_end]

#         # check if the right char is in pattern
#         if right_char in pattern_dict:
#             pattern_dict[right_char] -= 1
#             matched += 1

#         # shrink the window
#         if window_end >= len(pattern):
#             if left_char in pattern_dict:
#                 pattern_dict[left_char] += 1
#                 matched -= 1
#             window_start += 1
        
#         # check if the current matched window size matches that of the str length
#         if matched == len(pattern):
#             result_indexes.append(window_start)

    


