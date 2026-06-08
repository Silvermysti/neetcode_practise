class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.word_length=len(word)
        self.nrows=len(board)
        self.ncols=len(board[0])
        self.found=0

        def backtrack(current, row, col, visited):
            if current==self.word_length or self.found==1:
                if self.found==0:
                    self.found=1
                return

            if row+1<self.nrows and board[row+1][col]==word[current] and visited[row+1][col]==0:
                    visited[row+1][col]=1
                    #print(board[row+1][col], visited)
                    backtrack(current+1, row+1, col, visited)
                    visited[row+1][col]=0

            if col+1<self.ncols and board[row][col+1]==word[current] and visited[row][col+1]==0:
                    visited[row][col+1]=1
                    #print(board[row][col+1], visited)
                    backtrack(current+1, row, col+1, visited)
                    visited[row][col+1]=0

            if row>0 and board[row-1][col]==word[current] and visited[row-1][col]==0:
                    visited[row-1][col]=1  
                    #print(board[row-1][col], visited)           
                    backtrack(current+1, row-1, col, visited)
                    visited[row-1][col]=0

            #print(col-1, board[row][col-1], word[current])
            if col>0 and board[row][col-1]==word[current] and visited[row][col-1]==0:
                    visited[row][col-1]=1   
                    #print(board[row][col-1], visited)            
                    backtrack(current+1, row, col-1, visited)
                    visited[row][col-1]=0         

        visited=[[0]*self.ncols for _ in range(self.nrows)]
        for i in range(self.nrows):
            for j in range(self.ncols):
                if board[i][j]==word[0]:
                    visited[i][j]=1
                    #print(board[i][j], visited)
                    backtrack(1, i, j, visited)
                    visited[i][j]=0
        
        if self.found==1:
            return True
        return False
