# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.
# 把n!分解质因数：n! = 2^x * 3^y * 5^z * ...
# 其末尾0的个数等于min(x, z)
# 但是，在n!中，2出现的次数绝对是大于等于5出现的次数的，也就是说x肯定大于z


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            result += n // 5
            n //= 5
        return result
