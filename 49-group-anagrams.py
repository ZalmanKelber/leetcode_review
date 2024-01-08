# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from collections import defaultdict

class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frozen_dicts = defaultdict(lambda: [])
        for s in strs:
            char_count = defaultdict(lambda: 0)
            for ch in s:
                char_count[ch] += 1
            
            frozen_dicts[hashabledict(char_count)].append(s)
        output = []
        for fd in frozen_dicts:
            output.append(frozen_dicts[fd])
        return output