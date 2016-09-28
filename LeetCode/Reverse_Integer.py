# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# 很简单，但是需要注意整数的溢出


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = int(str(abs(x))[::-1])
        if result > 2147483647:
            return 0
        if x < 0:
            return - result
        return result
