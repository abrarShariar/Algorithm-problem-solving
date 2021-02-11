# SOLVED
def runLengthEncoding(string):
    # Write your code here.
    if len(string) == 0:
        return string
    if len(string) == 1:
        return "1"+string

    result_str = ""
    current_count = 0
    current_char = string[0]
    # loop over all the characters in the string
    for i in range(len(string)):
        if current_char != string[i]:
            result_str += str(current_count) + current_char
            current_char = string[i]
            current_count = 1
        else:
            # check if current_count is equal to 9 => we split
            if current_count == 9:
                result_str += str(current_count) + current_char
                current_count = 1
            else:
                current_count += 1

    result_str += str(current_count) + current_char

    return result_str


print(runLengthEncoding("AAABCD"))
print(runLengthEncoding("ABCCCCC"))
print(runLengthEncoding("AAAAAAAAAAAA"))


