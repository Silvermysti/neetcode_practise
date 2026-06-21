class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res=[]
        
        intervals.sort(key=lambda x: x[0])
        curr=None
        for i in range(len(intervals)):
            if i==0:
                curr=intervals[0]
                continue
            if intervals[i][0]<=curr[1]:
                curr=[curr[0], max(intervals[i][1], curr[1])]
            else:
                res.append(curr)
                curr=intervals[i]
            #print(curr, res)
        
        res.append(curr)
        return res