# Given an array of integers, every element appears twice except for one.
# Find that single one.
# 其实非常简单，只需要利用异或运算的性质就可以了


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
