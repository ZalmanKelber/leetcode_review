# https://leetcode.com/problems/triangle/description/?envType=study-plan-v2&envId=top-interview-150

# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        self.solutions = {}
        return self.recursive_minimumTotal((0, 0))
    def recursive_minimumTotal(self, idx: Tuple[int]) -> int:
        if idx not in self.solutions:
            row, column = idx
            cell = self.triangle[row][column]
            if row == len(self.triangle) - 1:
                self.solutions[idx] = cell
            else:
                self.solutions[idx] = cell + min(self.recursive_minimumTotal((row + 1, column)), self.recursive_minimumTotal((row + 1, column + 1)))
        return self.solutions[idx]
