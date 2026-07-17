class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        COLS=len(matrix[0])
        ROWS=len(matrix)
        self.presum=[[0]*(COLS+1) for _ in range(ROWS+1)]
        #print(self.presum)

        for r in range(1,ROWS+1):
            colsum=0
            for c in range(1,COLS+1):
                colsum+=matrix[r-1][c-1]
                #print(r,c)
                self.presum[r][c]= colsum + self.presum[r-1][c]
                #print(self.presum[r][c],r,c)
        for i in self.presum:
            print(i)
        #print(self.presum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:  
        r1,r2,c1,c2=row1+1,row2+1,col1+1,col2+1
        return self.presum[r2][c2] + self.presum[r1-1][c1-1] - self.presum[r1-1][c2] - self.presum[r2][c1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)