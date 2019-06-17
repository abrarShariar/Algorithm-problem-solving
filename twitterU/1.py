# solved

# Complete the braces function below.
def braces(values):
    # print(values)
    res = []
    for value in values:
        stack = []
        isValid = True

        # get each char
        for ch in value:
            start = ''
            if ch == '}':
                start = '{'
            elif ch == ']':
                start = '['
            elif ch == ')':
                start = '('

            if start != '':
                # start poping and check
                if len(stack) == 0:
                    isValid = False
                    break
                el = stack.pop()
                if el != start:
                    isValid = False
                    break
            else:
                stack.append(ch)

        if isValid && len(stack) == 0:
            res.append('YES')
        else:
            res.append('NO')

    return res

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)

    res = braces(values)
    print(res)

    # fptr.write('\n'.join(res))
    # fptr.write('\n')
    #
    # fptr.close()
