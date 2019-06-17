# SOLVED: https://www.hackerrank.com/challenges/sock-merchant?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
n = int(input())
dit = dict()
line = input().strip().split(' ')
pair_count = 0
for el in line:
    if el in dit:
        dit[el] = dit[el] + 1
        if dit[el]% 2 == 0:
            pair_count += 1
    else:
        dit[el] = 1

print(pair_count)
