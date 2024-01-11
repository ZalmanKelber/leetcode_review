# https://leetcode.com/problems/house-robber/submissions/1143551741/?envType=study-plan-v2&envId=top-interview-150

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        self.nums = nums
        self.cache = { 0: 0, 1: nums[0], 2: max(nums[0], nums[1]) }
        return self.recursive_rob(len(nums))
    
    def recursive_rob(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        left = self.nums[n - 1] + self.recursive_rob(n - 2)
        right = self.nums[n - 2] + self.recursive_rob(n - 3)
        result = max(left, right)
        self.cache[n] = result
        return result
    