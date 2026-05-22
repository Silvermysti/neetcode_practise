class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mini=0
        size=0
        counts={}

        for i in nums:
            if i not in counts:
                counts[i]=1
            else:
                counts[i]+=1

        n=0
        countsMax=sorted(counts.values())[-1:-k-1:-1]
        print(countsMax)
        
        res=[]
        n=0
        for i in counts:
            print(i)
            if counts[i] in countsMax:
                if n>k:
                    break
                res.append(i)
                n+=1
        
        return res