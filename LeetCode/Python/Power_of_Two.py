# Given an integer, write a function to determine if it is a power of two.
# 2的幂的数为1, 2， 4， 8， 16等等，注意观察它们的二进制表示：
# 0001, 0010, 0100, 1000, 00010000, 都是0001左移的结果，对应的他们各自减去1所得的二进制结果：
# 0000, 0001, 0011, 0111, 00001111, 可以看出使用&运算符的话结果都是0
# 所以有以下解法


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0
