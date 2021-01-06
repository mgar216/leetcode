"""
Runtime: 32 ms, faster than 82.10% of Python3 online submissions for Rotate Image.
Memory Usage: 14.3 MB, less than 51.10% of Python3 online submissions for Rotate Image.
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                holder = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = holder 
