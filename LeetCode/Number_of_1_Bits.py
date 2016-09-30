# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
# 思路:利用与运算的性质


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count, carry = 0, 1
        for i in range(32):
            if n & carry != 0:
                count += 1
            carry <<= 1
        return count
