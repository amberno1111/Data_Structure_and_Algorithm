#  Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Solve it without division and in O(n).
# For example, given [1,2,3,4], return [24,12,8,6].
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
# 思路：这道题给定一个数组，要求返回一个新数组，对于每一个位置上的数是其他位置上数的成绩，并且限定了时间复杂度为O(n)，而且不能用除法，如果让用除法的话，可以先遍历一遍数组求出所有的数字之积，然后再遍历一遍使用除法就行。
# 解决办法是执行两趟循环，要借用一个O(n)的数组，因此空间复杂度是O(n)
# 第一趟正向遍历数组，计算x 0 ~ x i-1 的乘积
# 第二趟反向遍历数组，计算x i+1 ~ x n-1 的乘积


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        result, num = [1], 1
        for i in range(1, len(nums)):
            num *= nums[i - 1]
            result.append(num)
        num = 1
        for i in range(len(nums)-1, 0, -1):
            num *= nums[i]
            result[i-1] *= num
        return result



















