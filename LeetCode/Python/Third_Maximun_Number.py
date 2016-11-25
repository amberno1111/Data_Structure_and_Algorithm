# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
# Example 1:
# Input: [3, 2, 1]
# Output: 1
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 思路： 首先用set的性质去掉重复的数，然后设置三个指针，分别记录最大值，第二大值和第三大值，在一次遍历过程中不断更新。还有，注意处理边界值-2147483648。


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(list(nums))
        else:
            nums = list(nums)
            first, second, third = -2147483648, -2147483648, -2147483648
            for i in range(len(nums)):
                if nums[i] > first:
                    first, second, third = nums[i], first, second
                elif nums[i] > second:
                    first, second, third = first, nums[i], second
                elif nums[i] > third:
                    third = nums[i]
            return third
















