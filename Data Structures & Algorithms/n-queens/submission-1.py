class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        positions=[['.' for _ in range(n)] for _ in range(n)]
        #print(positions)
        available=[set(range(n)) for _ in range(n)]

        def backtrack(available,row):
            #print(row, positions)
            if row==n:
                #print(positions)
                strings=["".join(s.copy()) for s in positions]
                #print(strings)
                res.append(strings)
                #print(res)
                return
            elif len(available[n-1])==0:
                return

            for col in available[row]:
                #print(row,col)
                positions[row][col]='Q'
                temp = [s.copy() for s in available]
                for j in range(row+1,n):
                    temp[j].discard(col)
                i=1
                while row+i<n:
                    if col+i<n:
                        temp[row+i].discard(col+i)
                    if col-i>=0:
                        temp[row+i].discard(col-i)
                    i+=1
                backtrack(temp,row+1)
                positions[row][col]='.'

        


        backtrack(available.copy(),0)
        return res

