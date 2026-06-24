class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        netrow=len(grid)
        netcol=len(grid[0])
        self.fresh=0
        self.time=0
        self.queue=deque()
    
        def traverse(row, col, mins):
            #print(self.time)

            self.fresh-=1
            '''print(row,col,mins)          
            print(self.fresh)
            print(" ")'''


            for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
                if 0<=row+i<netrow and 0<=col+j<netcol and grid[row+i][col+j]==1:
                    grid[row+i][col+j]=2
                    self.queue.append([row+i,col+j,mins+1])
                    '''for m in grid:
                        print(m)
                    print("")'''
            else:
                self.time=max(mins,self.time)



        for row in range(netrow):
            for col in range(netcol):
                if grid[row][col]==1:
                    self.fresh+=1
                elif grid[row][col]==2:
                    self.queue.append([row,col,0])
        
        ##print(self.fresh)
        if self.fresh==0:
            return 0
        if not self.queue:
            return -1
        while self.queue:
            params=self.queue.popleft()
            traverse(params[0],params[1],params[2])

        #print(self.fresh)
        if self.fresh>-1:
            return -1
        return self.time