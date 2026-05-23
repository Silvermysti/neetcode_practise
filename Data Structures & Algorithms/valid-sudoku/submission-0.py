class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsets=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
        columnsets=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
        gridsets=[set(),set(),set(),set(),set(),set(),set(),set(),set()]

        for row in range(9):
            gridrow = row//3

            for col in range(9):
                gridcol = col//3

                num=board[row][col]

                if num!=".":

                    grid=[(row)//3,(col)//3]
                    if grid==[0,0]:
                        grid=0;
                    elif grid==[0,1]:
                        grid=1
                    elif grid==[0,2]:
                        grid=2
                    elif grid==[1,0]:
                        grid=3
                    elif grid==[1,1]:
                        grid=4
                    elif grid==[1,2]:
                        grid=5
                    elif grid==[2,0]:
                        grid=6
                    elif grid==[2,1]:
                        grid=7
                    elif grid==[2,2]:
                        grid=8

                    if int(num)==1:
                        print(grid)


                    if (num in rowsets[row] or num in columnsets[col] or num in gridsets[grid]):
                        return False
                    rowsets[row].add(num)
                    columnsets[col].add(num)
                    gridsets[grid].add(num)
        
        return True















