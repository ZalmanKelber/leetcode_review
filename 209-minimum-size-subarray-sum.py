# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150

# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_pointer, right_pointer = 0, 0
        min_length = len(nums) + 1
        in_window = 0
        while right_pointer < len(nums):
            in_window += nums[right_pointer]
            if in_window >= target:
                while in_window - target >= nums[left_pointer]:
                    in_window -= nums[left_pointer]
                    left_pointer += 1
                min_length = min(min_length, right_pointer + 1 - left_pointer)
            right_pointer += 1
        return min_length if min_length <= len(nums) else 0