class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.res=[]
        def backtrack(string,_open,_close):
            if _open==n and _close==n:
                self.res.append(string)
                return

            if _open<n:
                backtrack(string+'(', _open+1, _close)
            if _close<n and _close<_open:
                backtrack(string+')', _open, _close+1)
            
        
        backtrack("",0,0)
        return self.res