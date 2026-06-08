class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        end=len(digits)
        if end==0:
            return []
        represent={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res=[]

        def backtrack(curr,arr):
            if curr==end:
                res.append("".join(arr))
                return            
            for i in represent[digits[curr]]:
                arr.append(i)
                backtrack(curr+1,arr)
                arr.pop()


        backtrack(0,[])
        return res