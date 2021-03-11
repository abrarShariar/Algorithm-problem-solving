# IN PROGRESS
def find_word_concatenation(str, words):
    result_indices = []

    word_len = len(words[0])
    window_size = (len(words) * word_len)

    # create the dictionary from the words list
    word_dict = {}
    for word in words:
        for ch in word:
            word_dict[ch] = word_dict.get(ch, 0) + 1


    window_start = 0
    matched = 0
    for window_end in range(len(str)):
        left_char = str[window_start]
        right_char = str[window_end]
        current_window_size = window_end - window_start + 1

        # if the window size is large => shirnk
        if current_window_size > window_size:
            # shrink steps goes here
            if left_char in word_dict:
                word_dict[left_char] += 1
                window_start += 1
                if word_dict[left_char] == 0:
                    matched -= 1
        else:
        # if window size is smaller => grow
            if right_char in word_dict:
                if word_dict[right_char] == 0:
                    if left_char in word_dict:
                        word_dict[left_char] += 1
                        window_start += 1
                        if word_dict[left_char] == 0:
                            matched += 1
                    
                word_dict[right_char] -= 1

        if word_dict[right_char] == 0:
            matched += 1

        if matched == len(word_dict):
            result_indices.append(window_start)
            matched = 0

    if matched == len(word_dict):
        result_indices.append(window_start)

    return result_indices

# print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))
print(find_word_concatenation("catfoxcat", ["cat", "fox"]))