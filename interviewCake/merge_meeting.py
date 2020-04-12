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


# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
