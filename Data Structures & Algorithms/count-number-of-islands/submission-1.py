class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        print(visited)
        netcols=len(grid[0])
        netrows=len(grid)


        def traverse(row,col):

            visited[row][col]=1
            for i in visited:
                print(i)
            print(" ")

            if row>0 and visited[row-1][col]!=1 and grid[row-1][col]!="0":
                traverse(row,col-1)
            if row+1<netrows and visited[row+1][col]!=1 and grid[row+1][col]!="0":
                traverse(row+1,col)
            if col>0 and visited[row][col-1]!=1 and grid[row][col-1]!="0":
                traverse(row,col-1)
            if col+1<netcols and visited[row][col+1]!=1 and grid[row][col+1]!="0":
                traverse(row,col+1)
            return


        res=0
        for row in range(netrows):
            for col in range(netcols):
                if grid[row][col]=="1" and visited[row][col]==0:
                    res+=1
                    traverse(row, col)
                    print("island ", res," complete")
                    print(" ")
                    print(" ")
                    
        

        return res