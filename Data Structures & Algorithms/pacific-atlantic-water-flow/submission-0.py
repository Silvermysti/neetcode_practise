class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        netrow=len(heights)
        netcol=len(heights[0])
        atl=set()
        pac=set()

        def traverse(row,col,visited):

            visited.add((row,col))

            for r,c in [[1,0],[-1,0],[0,1],[0,-1]]:
                nextrow=row+r
                nextcol=col+c
                if -1<nextrow<netrow and -1<nextcol<netcol and ((nextrow,nextcol) not in visited) and heights[row][col]<=heights[nextrow][nextcol]:
                    traverse(row+r,col+c,visited)

        for col in range(netcol):
            traverse(0,col,pac)
            traverse(netrow-1,col,atl)
        
        for row in range(netrow):
            traverse(row,0,pac)
            traverse(row,netcol-1,atl)
        
        #print(atl)
        #print(pac)
        
        res=[]
        for i in atl:
            if i in pac:
                res.append(list(i))
        #print(res)
        return res
