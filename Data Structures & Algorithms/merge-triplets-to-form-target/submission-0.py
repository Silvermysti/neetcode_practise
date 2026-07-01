class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        amax=bmax=cmax=0
        for i in triplets:
            if i[0]<=target[0] and i[1]<=target[1] and i[2]<=target[2]:
                amax=max(amax,i[0])
                bmax=max(bmax,i[1])
                cmax=max(cmax,i[2])
        if [amax,bmax,cmax]==target:
            return True
        return False