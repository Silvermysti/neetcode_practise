class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        netrow=len(matrix)
        netcol=len(matrix[0])
        visited=set()
        res=[]

        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(row,col,curr):
            res.append(matrix[row][col])
            visited.add((row,col))
            #print(res)
            for i in range(4):
                direction=directions[(curr+i)%4]
                nextrow=row+direction[0]
                nextcol=col+direction[1]
                if -1<nextrow<netrow and -1<nextcol<netcol and (nextrow,nextcol) not in visited:
                    dfs(nextrow,nextcol,curr+i)
                    return
            return

        dfs(0,0,0)    
        return res

