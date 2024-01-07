# https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices_by_value = {}
        dups = set()
        for i, num in enumerate(nums):
            if num in indices_by_value:
                indices_by_value[num].add(i)
                if len(indices_by_value[num]) > 2:
                    dups.add(i)
            else:
                indices_by_value[num] = { i }
        solutions = set()
        positive_indices = [i for i in range(len(nums)) if nums[i] >= 0 and i not in dups]
        negative_indices = [i for i in range(len(nums)) if nums[i] < 0 and i not in dups]
        for i in positive_indices:
            for j in negative_indices:
                k = 0 - nums[i] - nums[j]
                if k in indices_by_value:
                    idx_set = set(indices_by_value[k])
                    idx_set.discard(i)
                    idx_set.discard(j)
                    if len(idx_set) > 0:
                        solutions.add(tuple(sorted([nums[i], nums[j], k])))
        if 0 in indices_by_value and len(indices_by_value[0]) >= 3:
            solutions.add((0, 0, 0))
        return [list(s) for s in solutions]