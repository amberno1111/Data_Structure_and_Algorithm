# Given two arrays, write a function to compute their intersection.
# Example:
#   Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2]
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# 思路: 很简单,就是统计每个元素出现的次数,使用字典来保存,这里主要是利用字典的查找效率为O(1)的性质


# Time: O(m + n)
# Space: O(m + n)
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lookup, result = {}, []
        for i in nums1:
            if i in lookup.keys():
                lookup[i] += 1
            else:
                lookup[i] = 1
        for j in nums2:
            if j in lookup.keys() and lookup[j] > 0:
                result.append(j)
                lookup[j] -= 1
        return result




