def find_permutation(str, pattern):
    # TODO: Write your code here
    # create the pattern dict
    pattern_dict = {}
    for ch in pattern:
        pattern_dict[ch] = pattern_dict.get(ch, 0) + 1
    
    window_start = 0
    matched = 0
    # iterate over the chars on the str
    for window_end in range(len(str)):
        right_char = str[window_end]
        left_char = str[window_start]

        if right_char in pattern_dict:
            pattern_dict[right_char] -= 1
            matched += 1
        
        if window_end >= len(pattern):
            
            if left_char in pattern_dict:
                pattern_dict[left_char] += 1
                matched -= 1

            window_start += 1
        
        # check if all keys in patten_dict is 0
        if matched == len(pattern):
            return True
    
    return False

print(find_permutation("oidbcaf", "abc"))
print(find_permutation("odicf", "dc"))
print(find_permutation("bcdxabcdy", "bcdyabcdx"))