# NOT SOLVED
n = int(input())
points = []
for i in range(n):
    segment = tuple(map(int, input().split()))
    points.append(segment)

# sort based on the first coordinate
sorted_points = sorted(points, key=lambda x: x[0])
result_points = set()

for i in range(len(sorted_points) - 1):
    current_start = sorted_points[i][0]
    current_end = sorted_points[i][1]

    next_start = sorted_points[i+1][0]
    next_end = sorted_points[i+1][1]

    # overlapping
    if current_end >= next_start:
        if current_end <= next_end:
            result_points.add(current_end)
        else:
            result_points.add(next_end)

print(result_points)