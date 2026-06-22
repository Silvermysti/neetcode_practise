"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 1 or len(intervals) == 0:
            return True

        end=0
        intervals.sort(key=lambda x: x.start)
        for i in intervals:
            if end>i.start:
                return False
            else:
                end=max(end, i.end)
        return True
            