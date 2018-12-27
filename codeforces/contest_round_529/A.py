n = int(input())
s = input()

r_len = 0
i = 0
while i < len(s):
    end = i + r_len
    if end >= len(s):
        break
    sub = s[i:end+1]
    print(sub[0], end="")
    r_len += 1
    i = i + r_len
