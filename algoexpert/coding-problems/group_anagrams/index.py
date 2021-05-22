# SOLVED

# def groupAnagrams(words):
#     count_dict = {}
#     result_list = []
    
#     # O(n)
#     for index, word in enumerate(words):
#         word = ''.join(sorted(word))
#         count_dict[word] = count_dict.get(word, [])
#         count_dict[word].append(index)
    
#     # O(n)
#     for key, value in count_dict.items():
#         sub_list = []
#         for val in value:
#             sub_list.append(words[val])

#         result_list.append(sub_list)

#     return result_list


def groupAnagrams(words):
    count_dict = {}
    # O(n)
    for index, word in enumerate(words):
        sorted_word = ''.join(sorted(word))
        count_dict[sorted_word] = count_dict.get(sorted_word, [])
        count_dict[sorted_word].append(word)

    return list(count_dict.values())

input_list = ['yo', 'act', 'flop', 'tac', 'act', 'oy', 'olfp']
print(groupAnagrams(input_list))

