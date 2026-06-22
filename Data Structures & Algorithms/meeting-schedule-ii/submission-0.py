"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        roomEnds=[intervals[0].end]
        intervals.sort(key=lambda x:x.start)

        for i in range(1,len(intervals)):
            for j in range(len(roomEnds)):
                if intervals[i].start>=roomEnds[j]:
                    roomEnds[j]=intervals[i].end
                    break
            else:
                roomEnds.append(intervals[i].end)
            print(roomEnds)

        return len(roomEnds)