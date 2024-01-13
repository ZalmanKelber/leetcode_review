# https://leetcode.com/problems/unique-paths-ii/description/?envType=study-plan-v2&envId=top-interview-150

# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        self.grid = obstacleGrid
        self.solutions = { (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1): 1 }
        return self.num_paths((0, 0))

    def num_paths(self, idx: Tuple[int]) -> int:
        if idx not in self.solutions:
            row, column = idx
            if row < 0 or column < 0 or row >= len(self.grid) or column >= len(self.grid[0]) or self.grid[row][column] == 1:
                self.solutions[idx] = 0
            else:
                self.solutions[idx] = self.num_paths((row, column + 1)) + self.num_paths((row + 1, column))
        return self.solutions[idx]