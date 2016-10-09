# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# For example:
# given num = 16, return True; Given num = 5, return False


# 只要注意4的幂二进制排列的规律就行了
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 1
        for i in range(16):
            if n == num:
                return True
            n <<= 2
        return False
