# https://leetcode.com/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-interview-150

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences_by_bottom_element = {}
        sequences_by_top_element = {}
        for num in set(nums):
            if num + 1 in sequences_by_bottom_element and num - 1 in sequences_by_top_element:
                    top_el = sequences_by_bottom_element[num + 1] + num
                    bottom_el = num - sequences_by_top_element[num - 1]
                    length = top_el + 1 - bottom_el
                    del sequences_by_top_element[num - 1]
                    del sequences_by_bottom_element[num + 1]
                    sequences_by_bottom_element[bottom_el] = length
                    sequences_by_top_element[top_el] = length
            elif num - 1 in sequences_by_top_element:
                bottom_el = num - sequences_by_top_element[num - 1]
                sequences_by_top_element[num] = sequences_by_top_element[num - 1] + 1
                del sequences_by_top_element[num - 1]
                sequences_by_bottom_element[bottom_el] += 1
            elif num + 1 in sequences_by_bottom_element:
                top_el = sequences_by_bottom_element[num + 1] + num
                sequences_by_bottom_element[num] = sequences_by_bottom_element[num + 1] + 1
                del sequences_by_bottom_element[num + 1]
                sequences_by_top_element[top_el] += 1
            else:
                sequences_by_bottom_element[num] = 1
                sequences_by_top_element[num] = 1
        max_length = 0
        for bottom_el in sequences_by_bottom_element:
            max_length = max(max_length, sequences_by_bottom_element[bottom_el])
        return max_length