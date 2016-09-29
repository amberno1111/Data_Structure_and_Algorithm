# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# Write a function that will return true is the ransom note can be constructed from the magazines;
# otherwise, it will return false
# Each letter in the magazine string can only be used once in your ransom note.
# Note:
# You may assume that both strings contain only lowercase letters.
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lookup = {}
        for letter in magazine:
            if letter in lookup.keys():
                lookup[letter] += 1
            else:
                lookup[letter] = 1
        for letter in ransomNote:
            if letter in lookup.keys() and lookup[letter] > 0:
                lookup[letter] -= 1
            else:
                return False
        return True
