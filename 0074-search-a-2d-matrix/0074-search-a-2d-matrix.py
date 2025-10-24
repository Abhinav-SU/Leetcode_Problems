class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow = 0
        startCol = len(matrix[0])-1

        while startRow <=len(matrix)-1 and startCol >=0:
            if matrix[startRow][startCol]==target:
                return True
            elif matrix[startRow][startCol] < target:
                startRow+=1
            else:
                startCol-=1
        return False