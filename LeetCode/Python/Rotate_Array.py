# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
# 基本思路：以n-k为界，分别对数组两边进行一次逆置，然后对整个数组执行一次逆置
# For example：
# 数组 [1, 2, 3, 4, 5, 6, 7] 以 n-k=7-3=4为界，左右两边进行一次逆置，可以得到新数组：
# [4, 3, 2, 1, 7, 6, 5]，然后再对整个数组进行一次逆置，可得 [5, 6, 7, 1, 2, 3, 4]
# Time：O(n)


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)
        return nums

    def reverse(self, nums, start, end):
        while start < end - 1:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1
