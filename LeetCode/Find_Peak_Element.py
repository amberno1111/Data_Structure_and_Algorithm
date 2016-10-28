# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -∞.
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


# 思路1：顺序遍历，时间O(n)，空间O(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1


# 思路2：二分查找，时间O(log n)
# 由于两端都是服务穷，有上坡就必定有一个峰值，先看中点的两边大小，如果向左是上坡，就抛弃右边，如果向右是上坡，就抛弃左边，直到两边都比中间小，就是要找的元素了
class Solution1(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid+1 == len(nums) or nums[mid] > nums[mid + 1]):
                return mid
            elif not (mid == 0 or nums[mid-1] < nums[mid]):
                right = mid
            else:
                left = mid + 1
        return left


