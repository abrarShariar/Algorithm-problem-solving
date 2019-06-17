# SOLVED

def missingWords(s, t):
    # Write your code here
    s = s.split(' ')
    t = t.split(' ')
    cur_index = 0
    while len(t) != 0 and cur_index < len(s):
        if s[cur_index] == t[0]:
            t.pop(0)
            s.pop(cur_index)
        else:
            cur_index += 1

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    result = missingWords(s, t)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
