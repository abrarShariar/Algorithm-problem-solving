n = int(input())
for i in range(n):
    text = input()
    new_text = ['', '', '']
    if len(text) > 10:
        new_text[0] = text[0]
        new_text[1] = str(len(text) - 2)
        new_text[2] = text[len(text)-1]
        print(new_text[0] + new_text[1] + new_text[2])
    else:
        print(text)
