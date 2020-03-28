# Problem statement: https://leetcode.com/problems/minimum-number-of-refueling-stops/


from typing import List

def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    # if no stations are there, empty list
    n = len(stations)
    if startFuel >= target:
        return 0

    if n == 0:
        # check if start fuel is enough to go to the target
        if startFuel >= target:
            return 0
        else:
            return -1

    current = 0
    initial = 0
    fuelCount = 0
    fuel = startFuel

    while (current < n):
        while (stations[current][0] - initial <= fuel):
            current += 1
            if (current >= n): break

        if stations[current - 1][0] == initial:
            return -1

        fuel -= (stations[current - 1][0] - initial)
        print(fuel)
        initial = stations[current - 1][0]
        if current - 1 < n:
            fuelCount += 1
            fuel += stations[current - 1][1]

    if (target - stations[current - 1][0] > fuel):
        return -1
    else:
        return fuelCount


# print(minRefuelStops(1, 1, []))
# print(minRefuelStops(100, 1, [[10,100]]))
# print(minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]]))
# print(minRefuelStops(999, 1000, [[5,100],[997,100],[998,100]]))
print(minRefuelStops(100, 50, [[25,50],[50,25]]))
