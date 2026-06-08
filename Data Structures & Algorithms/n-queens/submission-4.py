class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        POSITIONS=[['.' for _ in range(n)] for _ in range(n)]
        available=[[1]*n for _ in range(n)]

        def backtrack(available,row):
            if row==n:
                res.append(["".join(s.copy()) for s in POSITIONS])
                return
            elif sum(available[n-1])==0:
                return

            for col in range(n):
                if available[row][col]==0:
                    continue
                POSITIONS[row][col]='Q'
                TEMPORARILY_AVAILABLE = [s.copy() for s in available]
                for j in range(row+1,n):
                    TEMPORARILY_AVAILABLE[j][col]=0
                i=1
                while row+i<n:
                    if col+i<n:
                        TEMPORARILY_AVAILABLE[row+i][col+i]=0
                    if col-i>=0:
                        TEMPORARILY_AVAILABLE[row+i][col-i]=0
                    i+=1
                backtrack(TEMPORARILY_AVAILABLE,row+1)
                POSITIONS[row][col]='.'

        backtrack(available,0)
        return res

