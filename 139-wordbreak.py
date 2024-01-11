# https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.solution_cache = {}
        self.s = s
        self.wordDict = wordDict
        return self.recursive_wordBreak(0)
    def recursive_wordBreak(self, n: int) -> bool:
        if n == len(self.s):
            return True
        if n not in self.solution_cache:
            i = n + 1
            while i <= len(self.s):
                if self.s[n:i] in self.wordDict and self.recursive_wordBreak(i):
                    self.solution_cache[n] = True
                i += 1
            if n not in self.solution_cache:
                self.solution_cache[n] = False
        return self.solution_cache[n]