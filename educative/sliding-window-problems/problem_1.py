def find_permutation(str, pattern):
    # TODO: Write your code here
    pattern_dict = {}
    for ch in pattern:
        pattern_dict[ch] = pattern_dict.get(ch, 0) + 1
    
    # slide over the string
    window_start = 0
    running_dict = {}

    # loop over the str
    for window_end in range(len(str)):
        if window_end >= len(pattern):
            running_dict[str[window_start]] = running_dict[str[window_start]] - 1
            if running_dict[str[window_start]] <= 0:
                del running_dict[str[window_start]]

            window_start += 1
        
        running_dict[str[window_end]] = running_dict.get(str[window_end], 0) + 1
        # check if the pattern matches
        if check_if_pattern_matches(running_dict, pattern_dict) == True:
            return True

    return check_if_pattern_matches(running_dict, pattern_dict)

def check_if_pattern_matches(running_dict, pattern_dict):
    if len(running_dict) != len(pattern_dict):
        return False

    for key, value in pattern_dict.items():
        if running_dict.get(key, -1) != value:
            return False
    
    return True



print(find_permutation("oidbcaf", "abc"))
print(find_permutation("odicf", "dc"))
print(find_permutation("bcdxabcdy", "bcdyabcdx"))