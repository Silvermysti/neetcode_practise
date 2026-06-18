class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        netcol=len(grid[0])
        netrow=len(grid)
        visited=[[0]*netcol for _ in range(netrow)]

        def traverse(distance,row,col):

            if grid[row][col]<distance:
                return
            else:
                grid[row][col]=distance
            '''for i in grid:
                print(i)
            print("")'''

            visited[row][col]=1
            if row>0 and visited[row-1][col]==0 and grid[row-1][col]!=-1 and grid[row-1][col]!=0:
                traverse(distance+1,row-1,col)
            if row+1<netrow and visited[row+1][col]==0 and grid[row+1][col]!=-1 and grid[row+1][col]!=0:
                traverse(distance+1,row+1,col)
            if col>0 and visited[row][col-1]==0 and grid[row][col-1]!=-1 and grid[row][col-1]!=0:
                traverse(distance+1,row,col-1)
            if col+1<netcol and visited[row][col+1]==0 and grid[row][col+1]!=-1 and grid[row][col+1]!=0:
                traverse(distance+1,row,col+1)
            visited[row][col]=0
            return

        for row in range(netrow):
            for col in range(netcol):
                if grid[row][col]==0:
                    #visited = [[0]*netcol for _ in range(netrow)]
                    traverse(0,row,col)
