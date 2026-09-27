class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row, col = len(matrix), len(matrix[0])
        rows, cols = [False] * row, [False] * col

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(row):
            for c in range(col):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0