# verbose and shitty

def cleanText(S):
    char_index = 0
    space_index = 1
    in_list = list(S)

    while char_index < len(in_list) and space_index < len(in_list):
        # if found backspace 
        if in_list[space_index] == '#':
            in_list[char_index] = '0'
            in_list[space_index] = '0'
            while char_index >=0 and in_list[char_index] == '0':
                char_index -= 1
            space_index += 1
        else:
            space_index += 1

        if space_index >= len(in_list) or char_index >= len(in_list):
            break

        if char_index < 0:
            char_index = space_index
            if in_list[char_index] == '#':
                in_list[char_index] = '0'
            space_index = space_index + 1

    return in_list

class Solution:
    def backspaceCompare(self, S, T) -> bool:
        s_list = cleanText(S)
        t_list = cleanText(T)

        print(s_list)
        print(t_list)

        res_s = ""
        res_t = ""
        for i in range(len(s_list)):
            if s_list[i] != '#' and s_list[i] != '0':
                res_s += s_list[i]

        for i in range(len(t_list)):
            if t_list[i] != '#' and t_list[i] != '0':
                res_t += t_list[i]

        if res_s == res_t:
            return True
        else:
            return False

# # ok
# cleanText("a#c#")

# # ok
# cleanText("a###")

# # ok
# cleanText("abc#")

# # ok
# cleanText("####")

# # ok
# cleanText("a##c")

# # ok
# cleanText("abcdef#")

# # ok
# cleanText("ab#")

# # ok
# cleanText("a#")

x = Solution()
x.backspaceCompare("a#c", "b")
x.backspaceCompare("a##c", "#a#c")
x.backspaceCompare("ab##", "c#d#")
x.backspaceCompare("bxj##tw","bxo#j##tw")






        