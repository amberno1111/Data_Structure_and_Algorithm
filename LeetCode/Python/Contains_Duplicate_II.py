# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
# 思路: 很简单,使用一个字典来保存扫描过的数及其索引,然后对整个数组进行一次遍历,检查当前扫描到的数num是否已经出现过,如果是,则比较两个数之间的索引之差,小于k则返回True, 否则更新num的索引,然后继续扫描,直到扫描完整个数组或找到符合条件的数为止.
# 时间复杂度O(n), 空间复杂度O(n)


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            else:
                if i - lookup[num] <= k:
                    return True
                lookup[num] = i
        return False
