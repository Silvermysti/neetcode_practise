"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        n=len(intervals)
        if n==0:
            return 0
        if n==1:
            return 1

        intervals.sort(key=lambda x:x.start)
        roomEnds=[intervals[0].end]

        for i in range(1,n):
            for j in range(len(roomEnds)):
                if intervals[i].start>=roomEnds[j]:
                    roomEnds[j]=intervals[i].end
                    break
            else:
                roomEnds.append(intervals[i].end)
            print(roomEnds)

        return len(roomEnds)