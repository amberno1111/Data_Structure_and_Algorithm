# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Examples:
# s = "leetcode"
# return 0.
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.
# 思路:还是使用字典保存出现过的字母的次数,然后再重新遍历一遍字符串,返回最早出现的次数为1的字母


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        for letter in s:
            if letter in lookup.keys():
                lookup[letter] += 1
            else:
                lookup[letter] = 1
        for index, letter in enumerate(s):
            if lookup[letter] == 1:
                return index
        return -1
