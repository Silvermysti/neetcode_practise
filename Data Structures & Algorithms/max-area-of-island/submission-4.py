class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.maxarea=0
        self.area=0
        netcol=len(grid[0])
        netrow=len(grid)
        visited=[[0]*netcol for _ in range(netrow)]
        #print(visited)



        def traverse(row,col):
            visited[row][col]=1
            '''for i in visited:
                print(i)
            print(" ")'''
            self.area+=1
            

            if row>0 and grid[row-1][col]==1 and visited[row-1][col]==0:
                traverse(row-1,col)
            if row+1<netrow and grid[row+1][col]==1 and visited[row+1][col]==0:
                traverse(row+1,col)
            if col>0 and grid[row][col-1]==1 and visited[row][col-1]==0:
                traverse(row,col-1)
            if col+1<netcol and grid[row][col+1]==1 and visited[row][col+1]==0:
                traverse(row,col+1)


        for row in range(netrow):
            for col in range(netcol):
                if grid[row][col]==1 and visited[row][col]==0:
                    traverse(row,col)
                    if self.area>self.maxarea:
                        self.maxarea=self.area
                    #print("island complete, area: ", self.area, ", maxarea: ", self.maxarea)
                    #print("")
                    self.area=0

        return self.maxarea
