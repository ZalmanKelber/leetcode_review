# https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        indices_by_height = {}
        max_height = 0
        total_water = 0
        for i, h in enumerate(height):
            max_height = max(max_height, h)
            if h in indices_by_height:
                indices_by_height[h].append(i)
            else:
                indices_by_height[h] = [i]
        right_pointer = indices_by_height[max_height][0]
        left_pointer = indices_by_height[max_height][0]
        def find_next_highest_to_right(right_pointer):
            h = height[right_pointer]
            idx = indices_by_height[h].index(right_pointer)
            if idx < len(indices_by_height[h]) - 1:
                return indices_by_height[h][idx + 1]
            h -= 1
            while h not in indices_by_height or indices_by_height[h][-1] < right_pointer:
                h -= 1
            for next_h in indices_by_height[h]:
                if next_h > right_pointer:
                    return next_h
        def find_next_highest_to_left(left_pointer):
            h = height[left_pointer]
            idx = indices_by_height[h].index(left_pointer)
            if idx > 0:
                return indices_by_height[h][idx - 1]
            h -= 1
            while h not in indices_by_height or indices_by_height[h][0] > left_pointer:
                h -= 1
            for i in range(len(indices_by_height[h])):
                if indices_by_height[h][-1 - i] < left_pointer:
                    return indices_by_height[h][-1 - i]
        while right_pointer < len(height) - 1:
            next_highest = find_next_highest_to_right(right_pointer)
            for i in range(right_pointer + 1, next_highest):
                total_water += height[next_highest] - height[i]
            right_pointer = next_highest
        while left_pointer > 0:
            next_highest = find_next_highest_to_left(left_pointer)
            for i in range(next_highest + 1, left_pointer):
                total_water += height[next_highest] - height[i]
            left_pointer = next_highest
        return total_water