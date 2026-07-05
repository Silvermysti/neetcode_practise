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
                if -1<row+direction[0]<netrow and -1<col+direction[1]<netcol and (row+direction[0],col+direction[1]) not in visited:
                    dfs(row+direction[0],col+direction[1],curr+i)
                    return
            return

        dfs(0,0,0)    
        return res

