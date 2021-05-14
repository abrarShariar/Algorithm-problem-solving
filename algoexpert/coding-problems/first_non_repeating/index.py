def firstNonRepeatingCharacter(input_str):
    dict = {}
    # go over all the char in the input_str => create a dictionary of frequencies
    for ch in input_str:
        dict[ch] = dict.get(ch, 0) + 1

    # if the dictionary value is non repeating => return 1
    for i in range(len(input_str)):
        if dict[input_str[i]] == 1:
            return i

    return -1
    
input_list = [
    "abrar",
    "test",
    "aaaa"
]

for item in input_list:
    print(firstNonRepeatingCharacter(item))