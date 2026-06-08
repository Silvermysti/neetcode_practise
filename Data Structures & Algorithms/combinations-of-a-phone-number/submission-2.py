class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        end=len(digits)
        if end==0:
            return []
        represent={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
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