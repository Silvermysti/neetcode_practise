class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mini=0
        size=0
        counts=[0]*1001

        for i in nums:
            counts[i]+=1

        set_=set()

        n=0
        countsMax=sorted(counts)[-1:-k-1:-1]
        print(countsMax)
        
        res=[]
        n=0
        for i,j in enumerate(counts):
            print(i)
            if j in countsMax:
                if n>k:
                    break
                res.append(i)
                n+=1
        
        return res