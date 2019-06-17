# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


n = int(input())
track = input()
track_stack = []
valley_count = 0
for el in track:
    if el == 'D':
        track_stack.append(el)
    elif el == 'U' and len(track_stack) != 0:
        # pop and test if valley
        track_stack.pop();
        if len(track_stack) == 0:
            valley_count += 1

print(track_stack)
print(valley_count)
