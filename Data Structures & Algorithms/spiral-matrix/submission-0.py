class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        netrow=len(matrix)
        netcol=len(matrix[0])
        visited=set()
        res=[]

        disp=0
        def dfs(row,col):
            res.append(matrix[row][col])
            visited.add(matrix[row][col])
            #print(res)

            if col+1<netcol and matrix[row][col+1] not in visited:
                dfs(row,col+1)
            elif row+1<netrow and matrix[row+1][col] not in visited:
                dfs(row+1,col)
            elif -1<col-1 and matrix[row][col-1] not in visited:
                dfs(row,col-1)
            elif -1<row-1 and matrix[row-1][col] not in visited:
                dfs(row-1,col)
            return

        dfs(0,0)    
        return res

