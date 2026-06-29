class Solution:
    def solve(self, board: List[List[str]]) -> None:
        netrow=len(board)
        netcol=len(board[0])
        visited=set()
        
        def traverse(row,col):

            visited.add((row,col))

            for r,c in [[1,0],[-1,0],[0,1],[0,-1]]:
                nextrow=row+r
                nextcol=col+c
                if -1<nextrow<netrow and -1<nextcol<netcol and board[nextrow][nextcol]=='O' and (nextrow,nextcol) not in visited:
                    traverse(nextrow,nextcol)
            
        for col in range(netcol):
            if board[0][col]=='O':
                traverse(0,col)
            if board[netrow-1][col]=='O':
                traverse(netrow-1,col)
        
        for row in range(netrow):
            if board[row][0]=='0':
                traverse(row,0)
            if board[row][netcol-1]=='O':
                traverse(row,netcol-1)

        for row in range(1,netrow-1):
            for col in range(1,netcol-1):
                if board[row][col]=='O' and (row,col) not in visited:
                    board[row][col]='X'
