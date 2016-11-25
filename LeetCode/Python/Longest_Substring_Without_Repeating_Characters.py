# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 利用队列解题
from collections import deque


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = deque()
        longest = 0
        for c in s:
            if c in chars:
                length = len(chars)
                if length > longest:
                    longest = length
                while chars.popleft() != c:
                    pass
            chars.append(c)
        return max(longest, len(chars))
