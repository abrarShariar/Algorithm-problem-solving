
# SOLUTION FROM interviewcake
def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)
    merged_meetings = [sorted_meetings[0]]

    for current_start, current_end in sorted_meetings[1:]:
        last_start, last_end = merged_meetings[-1]
        # merging meetings
        if current_start <= last_end:
            # when the next meeting is within the limit of the present meeting
            merged_meetings[-1] = (last_start, max(current_end, last_end))
        else:
            # creeate new meeting slot
            merged_meetings.append((last_start, current_end))

    return merged_meetings
