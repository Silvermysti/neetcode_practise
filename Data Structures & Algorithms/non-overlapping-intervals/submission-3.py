class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        res=0
        #reslist=[intervals[0]]
        last=intervals[0]
        for index in range(1,len(intervals)):

            #print(last, intervals[index])
            if last[1]>intervals[index][0]:
                res+=1
                if intervals[index][1]<last[1]:
                    #reslist[-1]=intervals[index]
                    last=intervals[index]
            else:
                #reslist.append(intervals[index])
                last=intervals[index]
            #print (reslist)
            #print(" ")
            #print (reslist)

        return res