# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k > 0:
            stored = [0] * k
            for i in range(len(nums) + k):
                hold = nums[i % len(nums)]
                nums[i % len(nums)] = stored[i % k]
                stored[i % k] = hold