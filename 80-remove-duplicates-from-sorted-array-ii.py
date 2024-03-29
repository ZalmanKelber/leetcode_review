# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        immediate_prev, further_prev = None, None
        shift = 0
        for i in range(len(nums)):
            if nums[i] == immediate_prev and nums[i] == further_prev:
                shift += 1
            elif nums[i] == immediate_prev:
                further_prev = immediate_prev
                nums[i - shift] = nums[i]
            else:
                immediate_prev = nums[i]
                further_prev = None
                nums[i - shift] = nums[i]
        return len(nums) - shift