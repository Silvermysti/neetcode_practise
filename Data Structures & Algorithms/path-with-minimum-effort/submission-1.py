class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        netrow=len(heights)
        netcol=len(heights[0])
        grid=[[float('inf') for i in range(netcol)] for _ in range(netrow)]
        grid[0][0]=0
        queue=deque()
        queue.append([0,0,0])

        while queue:
            dist,row,col=queue.popleft()
            #print(dist,row,col)
            for r,c in [[1,0],[0,1],[-1,0],[0,-1]]:
                newrow=row+r
                newcol=col+c
                if -1<newrow<netrow and -1<newcol<netcol:
                    newdist=max(dist,abs(heights[newrow][newcol]-heights[row][col]))
                    if grid[newrow][newcol]>newdist:
                        grid[newrow][newcol]=newdist
                        queue.append([newdist,newrow,newcol])
            '''
            for i in grid:
                print(i)
            print(" ")
            '''

        return grid[netrow-1][netcol-1]
        
