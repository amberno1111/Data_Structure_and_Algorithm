# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False
        lookup = {}
        for i, letter in enumerate(pattern):
            if letter not in lookup.keys():
                if str_list[i] not in lookup.values():
                    lookup[letter] = str_list[i]
                else:
                    return False
            elif lookup[letter] != str_list[i]:
                return False
        return True


