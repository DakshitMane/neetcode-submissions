class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        top, bot = 0, n - 1

        while top < bot:
            for col in range(n):
                matrix[top][col], matrix[bot][col] = matrix[bot][col], matrix[top][col]
            top += 1
            bot -= 1

        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]