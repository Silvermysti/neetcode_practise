class Solution:
    def partition(self, s: str) -> List[List[str]]:

            self.res=[]
            self.slength=len(s)

            def backtrack(current, arr):
                if current==self.slength:
                    for i in arr:
                        if i!=i[::-1]:
                            return
                    self.res.append(arr)
                    return
                    
                #combine
                temp=arr.copy()
                temp[-1]+=s[current]
                backtrack(current+1,temp)
                #start new
                temp=arr.copy()
                temp.append(s[current])
                backtrack(current+1,temp)
            


            backtrack(1,[s[0]])

            return self.res