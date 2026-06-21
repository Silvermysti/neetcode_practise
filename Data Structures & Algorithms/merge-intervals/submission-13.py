class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        stack = [intervals[0]]

        for s, e in intervals:
            last_end = stack[-1][1]
            if stack[-1][1] >= s:
                stack[-1][1] = max(last_end, e)
            else:
                stack.append([s, e])
        
        return stack
        