# https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=study-plan-v2&envId=top-interview-150

# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        found_substrings = []
        def is_substring(idx):
            found_words = {}
            for i in range(len(words)):
                word = s[idx + i * len(words[0]): idx + i * len(words[0]) + len(words[0])] 
                if word in word_dict and (word not in found_words or found_words[word] < word_dict[word]):
                    if word in found_words:
                        found_words[word] += 1
                    else:
                        found_words[word] = 1
                else:
                    return False
            return True 
        i = 0
        while i <= len(s) - len(words) * len(words[0]):
            if is_substring(i):
                found_substrings.append(i)
            i += 1
        return found_substrings