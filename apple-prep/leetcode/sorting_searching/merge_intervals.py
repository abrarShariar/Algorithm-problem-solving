# SOLVED!
class Solution:
    def merge(self, intervals):
        # first sort by the starting time
        intervals.sort()
        running_start_time = 0
        running_end_time = 0
        result_list = [intervals[0]]

        for i in range(1, len(intervals)):
            [current_start_time, current_end_time] = result_list[len(result_list) - 1]
            [running_start_time, running_end_time] = intervals[i]
            # if the current start time is less than or equal to the previous end_time => we merge
            if running_start_time <= current_end_time:
                current_start_time = min(current_start_time, running_start_time)
                current_end_time = max(current_end_time, running_end_time)
                result_list[len(result_list) - 1] = [current_start_time, current_end_time]
            else:
                result_list.append([running_start_time, running_end_time])

        return result_list

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))