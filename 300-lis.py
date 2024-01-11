# https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.cache = {}
        self.lis = 0
        for n in range(len(nums) - 1, -1, -1):
            self.fill_cache(n)
        return self.lis