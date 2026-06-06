class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distdict={}
        for i in points:
            dist=i[0]**2+i[1]**2
            if dist in distdict:
                distdict[dist].append(i)
            else:
                distdict[dist]=[i]

        n=0
        res=[]
        for i in sorted(distdict.keys()):
            if n==k:
                break
            for j in distdict[i]:
                res.append(j)
                n+=1
                if n==k:
                    break
        
        return res