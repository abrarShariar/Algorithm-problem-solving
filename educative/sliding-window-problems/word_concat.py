# def find_word_concatenation(str1, words):
#   if len(words) == 0 or len(words[0]) == 0:
#     return []

#   word_frequency = {}

#   for word in words:
#     if word not in word_frequency:
#       word_frequency[word] = 0
#     word_frequency[word] += 1

#   result_indices = []
#   words_count = len(words)
#   word_length = len(words[0])

#   for i in range((len(str1) - words_count * word_length)+1):
#     words_seen = {}
#     for j in range(0, words_count):
#       next_word_index = i + j * word_length
#       # Get the next word from the string
#       word = str1[next_word_index: next_word_index + word_length]
#       if word not in word_frequency:  # Break if we don't need this word
#         break

#       # Add the word to the 'words_seen' map
#       if word not in words_seen:
#         words_seen[word] = 0
#       words_seen[word] += 1

#       # No need to process further if the word has higher frequency than required
#       if words_seen[word] > word_frequency.get(word, 0):
#         break

#       if j + 1 == words_count:  # Store index if we have found all the words
#         result_indices.append(i)

#   return result_indices


# def main():
#   print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
#   print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


# main()



def find_word_concatenation(str, words):
    result_indices = []
    word_dict = {}
    
    # create the dictionary with words
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1

    # initialize the words seen
    words_seen = {}

    # define variables for word_count and word_length
    total_words = len(words)
    word_length = len(words[0])

    window_start = 0
    window_end = word_length - 1

    while window_end < len(str):
        # slice out the current word
        current_word = str[window_start: window_end + 1]

        # check if the current word is part of the word_dict
        if current_word in word_dict:
            words_seen[current_word] = words_seen.get(current_word, 0) + 1

            # if the words_seen is equal to the words => updated matched
            if words_seen[current_word] == word_dict[current_word]:
                result_indices.append(window_start)

            # if we got a word...go for the next
            window_start = window_end 
            window_end = (window_start + word_length) - 1
        
        else:
            window_end = (window_start + word_length) - 1
            window_start += 1


    return result_indices


print(find_word_concatenation("catfoxcat", ["cat", "fox"]))