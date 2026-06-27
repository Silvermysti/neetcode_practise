class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        if sum(gas)-sum(cost)<0:
            return -1

        n=len(cost)

        i=0
        while gas[i]-cost[i]<0:
            i+=1

        start=i
        end=(i+1)%n
        curr=gas[i]-cost[i]

        while start!=end:
            if curr<0 or curr+gas[end]-cost[end]<0:
                start= start-1 if (start-1>-1) else n-1
                curr+=gas[start]-cost[start]
            else:
                curr+=gas[end]-cost[end]
                end=(end+1)%n

        return start

