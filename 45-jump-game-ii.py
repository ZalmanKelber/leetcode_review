# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

class Solution:
    def jump(self, nums: List[int]) -> int:
        self.solved = {}
        self.nums = nums
        return self.recursiveJump(0)

    def recursiveJump(self, idx):
        if idx == len(self.nums) - 1:
            return 0
        if idx >= len(self.nums):
            return len(self.nums)
        min_jumps = len(self.nums)
        for next_idx in range(idx + 1, idx + 1 + self.nums[idx]):
            num_jumps = self.solved[next_idx] if next_idx in self.solved else self.recursiveJump(next_idx)
            if num_jumps < min_jumps:
                min_jumps = num_jumps
        self.solved[idx] = min_jumps + 1
        return min_jumps + 1