# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        in_sub_string = {}
        right_pointer, left_pointer = 0, 0
        while right_pointer < len(s):
            while s[right_pointer] in in_sub_string and in_sub_string[s[right_pointer]] > 0:
                in_sub_string[s[left_pointer]] -= 1
                left_pointer += 1
            if s[right_pointer] in in_sub_string:
                in_sub_string[s[right_pointer]] += 1
            else:
                in_sub_string[s[right_pointer]] = 1
            right_pointer += 1
            longest = max(longest, right_pointer - left_pointer)
        return longest