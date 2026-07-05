class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows=len(matrix)
        cols=len(matrix[0])
        visited=set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0 and (row,col) not in visited:
                    for c in range(cols):
                        if matrix[row][c]!=0:
                            visited.add((row,c))
                            matrix[row][c]=0
                    for r in range(rows):
                        if matrix[r][col]!=0:
                            visited.add((r,col))
                            matrix[r][col]=0

        