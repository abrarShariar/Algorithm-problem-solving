# OK

# import unittest
#
# START_TIME = 0
# END_TIME = 1
# def merge_ranges(meetings):
#     # sort tupples based on key 0
#     sorted(meetings, key=lambda x: x[0])
#     start_index = 0
#     resultList = []
#     while start_index < len(meetings):
#         next_index = start_index + 1
#         current_index = start_index
#         end_time = meetings[current_index][END_TIME]
#         if next_index < len(meetings):
#             while meetings[next_index][START_TIME] <= end_time and next_index < len(meetings):
#                 end_time = max(meetings[next_index][END_TIME], meetings[current_index][END_TIME])
#                 next_index += 1
#                 current_index = next_index
#                 if next_index >= len(meetings):
#                     break
#
#         resultList.append((meetings[start_index][START_TIME],end_time))
#         start_index = current_index + 1
#
#     return resultList
#
#
#
#

import unittest

START_TIME = 0
END_TIME = 1
def merge_ranges(meetings):
    # sort tupples based on key 0
    meetings = sorted(meetings, key=lambda x: x[0])
    print(meetings)
    current = 0
    next = current + 1
    resultList = []
    end_time = meetings[current][END_TIME]
    while current < len(meetings):
        start = current
        if next < len(meetings):
            while end_time >= meetings[next][START_TIME]:
                end_time = max(end_time, meetings[next][END_TIME])
                start += 1
                next += 1
                if next >= len(meetings):
                    break
        else:
            end_time = meetings[next - 1][END_TIME]

        resultList.append((meetings[current][START_TIME], end_time))
        if next < len(meetings):
            end_time = max(meetings[current][END_TIME], meetings[next][END_TIME])
        current = next
        next += 1

    return resultList


#
# print(merge_ranges([(1, 2), (2, 3)]))
# print(merge_ranges([(1, 5), (2, 3)]))
# # FIX
# print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))
# print(merge_ranges([(5, 6), (6, 8)]))
# print(merge_ranges([(1, 8), (2, 5)]))
#
# print(merge_ranges([(1, 3), (4, 8)]))
# print(merge_ranges([(1, 4),(2, 5),(5, 8)]))
#
print(merge_ranges([(5, 8), (1, 4), (6, 8)]))
#
# print(merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)]))
# print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
