# https://leetcode.com/problems/minimum-window-substring/?envType=study-plan-v2&envId=top-interview-150

# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count = defaultdict(lambda: 0)
        for ch in t:
            char_count[ch] += 1
        min_length, index = len(s) + 1, -1
        left_pointer, right_pointer = 0, 0
        in_window = defaultdict(lambda: 0)
        not_all_in_window = True
        def is_all_in_window():
            for ch in char_count:
                if in_window[ch] < char_count[ch]:
                    return False
            return True
        while right_pointer < len(s):
            in_window[s[right_pointer]] += 1
            if not_all_in_window and is_all_in_window():
                not_all_in_window = False
            if not not_all_in_window:
                while char_count[s[left_pointer]] < in_window[s[left_pointer]]:
                    in_window[s[left_pointer]] -= 1
                    left_pointer += 1
                window_length = right_pointer + 1 - left_pointer
                if window_length < min_length:
                    min_length, index = window_length, left_pointer
            right_pointer += 1
        if index == -1:
            return ''
        return s[index: index + min_length]