class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        positions=[['.' for _ in range(n)] for _ in range(n)]
        available=[[1]*n for _ in range(n)]
        #print(available)

        def backtrack(available,row):
            #print(available,row)
            if row==n:
                strings=["".join(s.copy()) for s in positions]
                res.append(strings)
                return
            elif sum(available[n-1])==0:
                #print("returned")
                return

            for col in range(n):
                if available[row][col]==0:
                    #print(available[row][col],"true")
                    continue
                positions[row][col]='Q'
                temp = [s.copy() for s in available]
                for j in range(row+1,n):
                    temp[j][col]=0
                i=1
                while row+i<n:
                    if col+i<n:
                        temp[row+i][col+i]=0
                    if col-i>=0:
                        temp[row+i][col-i]=0
                    i+=1
                #print(row, col, temp)
                backtrack(temp,row+1)
                positions[row][col]='.'
                #print("")

        backtrack(available,0)
        return res

