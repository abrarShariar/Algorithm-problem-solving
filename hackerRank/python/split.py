def split_and_join(line):
    # write your code here
    res = line.split(" ")
    return "-".join(res)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
