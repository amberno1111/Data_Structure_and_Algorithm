# Write a function that takes a string as input and reverse only the vowels of a string.
# Example 1:
# Given s = "hello", return "holle".
# Example 2:
# Given s = "leetcode", return "leotcede".
# Note:
# The vowels does not include the letter "y".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        first, last = 0, len(s) - 1
        lookup = 'aeiouAEIOU'
        s_list = list(s)
        while first < last:
            if s_list[first] in lookup and s_list[last] in lookup:
                s_list[first], s_list[last] = s_list[last], s_list[first]
                first += 1
                last -= 1
            elif s_list[first] in lookup and s_list[last] not in lookup:
                last -= 1
            elif s_list[first] not in lookup and s_list[last] in lookup:
                first += 1
            elif s_list[first] not in lookup and s_list[last] not in lookup:
                first += 1
                last -= 1
        return ''.join(s_list)
