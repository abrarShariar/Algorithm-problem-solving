def swap_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        else:
            result += ch.lower()
            
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
