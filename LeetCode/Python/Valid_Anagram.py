# Given two strings s and t, write a function to determine if t is an anagram of s.
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# Note:
# You may assume the string contains only lowercase alphabets.
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
# Subscribe to see which companies asked this question
# 解决思路,用一个字典来保存字符串中字母出现过的次数, 可以参考Ransom Note的解法,基本一致


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        lookup = {}
        for letter in s:
            if letter in lookup.keys():
                lookup[letter] += 1
            else:
                lookup[letter] = 1
        for letter in t:
            if letter in lookup.keys() and lookup[letter] > 0:
                lookup[letter] -= 1
            else:
                return False
        return True
