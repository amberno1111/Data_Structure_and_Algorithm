# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# For example,
# Given nums = [0, 1, 3] return 2.
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
# 思路：利用异或运算的性质，一个数自己异或自己是0


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        for i in range(len(nums)):
            result = result ^ i ^ nums[i]
        return result
