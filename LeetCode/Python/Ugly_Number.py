# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
# Note that 1 is typically treated as an ugly number.


# 解题的策略就是不断的去除以2， 3， 5这三个数，如果得到的最终结果时1，那么就是ugly数
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        for i in [2, 3, 5]:
            while (num % i) == 0:
                num /= i
        return num == 1
