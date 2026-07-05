class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows=len(matrix)
        cols=len(matrix[0])
        zerorow=set()
        zerocol=set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    zerorow.add(row)
                    zerocol.add(col)
        
        for col in zerocol:
            for r in range(rows):
                matrix[r][col]=0
        for row in zerorow:
            for c in range(cols):
                matrix[row][c]=0
        