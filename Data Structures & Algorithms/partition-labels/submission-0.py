class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        freq=Counter(s)
        print(freq)
        ind=0
        queue=set()
        res=[]

        curr=[0,0]

        while ind<len(s):
            if freq[s[ind]]>=1:
                curr[0]=ind
                freq[s[ind]]-=1
                if freq[s[ind]]>0:
                    queue.remove(s[ind])
                queue.add(s[ind])
                ind+=1
                while queue:
                    if freq[s[ind]]>1:
                        queue.add(s[ind])
                        freq[s[ind]]-=1
                        if freq[s[ind]]==0:
                            queue.remove(s[ind])
                        ind+=1
                curr[1]=ind
                res.append(curr[1]-curr[0])
            else:
                res.append(1)
                ind+=1



        return [[]]