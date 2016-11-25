# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
# 思路：设置双指针，从前往后遍历，先找到一个区间使得其值大于等于s，保存这个区间的长度，然后移动first指针直到区间的值小于s，再移动last指针找到一个新的区间使其值大于等于s，保存区间长度并与上一个区间长度进行比较，取小的这一个，然后按照前面的步骤继续往后遍历，直到便利完整个数组


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start, tmp, min_size = 0, 0, float("inf")
        for i in range(len(nums)):
            tmp += nums[i]
            while tmp >= s:
                min_size = min(min_size, i - start + 1)
                tmp -= nums[start]
                start += 1
        return min_size if min_size != float("inf") else 0



