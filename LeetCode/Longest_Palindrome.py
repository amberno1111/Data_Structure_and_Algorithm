# Given an string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.
# Note: Assume the length of given string will not exceed 1010
# Example:
# Input:
# "abccccdd"
# Output:
# 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 思路:实际上是对字符串里出现过的字母个数进行统计,使用一个字典保存出现过的字母的次数
#   如果一个字母出现的次数大于2次,则肯定能形成回文子串, count可以用次数//2来计算,比如出现3次,则count = 1, 出现4次则可以形成两次回文即aaaa,以此类推


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup, count = {}, 0
        for letter in s:
            if letter in lookup.keys():
                lookup[letter] += 1
            else:
                lookup[letter] = 1
        for k, v in lookup.items():
            if v >= 2:
                count += v // 2
        result = count * 2
        if len(s) > result:
            result += 1
        return result

