class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.end=len(digits)
        if self.end==0:
            return []
        self.represent={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        self.res=[]

        def backtrack(curr,arr):
            if curr==self.end:
                self.res.append("".join(arr))
                return
            
            for i in self.represent[digits[curr]]:
                arr.append(i)
                backtrack(curr+1,arr)
                arr.pop()


        backtrack(0,[])

        return self.res