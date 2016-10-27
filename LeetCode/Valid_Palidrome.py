# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
# For example
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# Note:
#   Have you consider the string might be empty? This is a good question to ask during an interview.
#   For the purpose of this problem, we define empty string as valid palindrome.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 注意isalpha()和isalnum()的区别
        s = ''.join([i.lower() for i in s if i.isalnum()])
        return s == s[::-1]
