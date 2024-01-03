# https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.visited = {0}
        self.nums = nums
        idx = 0
        return self.recursiveCanJump(idx)

    def recursiveCanJump(self, idx):
        if idx == len(self.nums) - 1:
            return True
        self.visited.add(idx)
        for next_idx in range(idx + 1, idx + 1 + self.nums[idx]):
            if next_idx not in self.visited and self.recursiveCanJump(next_idx):
                return True
        return False