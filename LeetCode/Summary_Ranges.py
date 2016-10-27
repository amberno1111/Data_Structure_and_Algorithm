# Given a sorted integer array without duplicates, return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
# 思路：题意是总结区间，如果是连续的，则合并为一个区间，返回首尾两个数并用'->'连接，如果不是，则返回单独的数
# 遍历一遍数组即可，每次判断下一个数是不是递增的，如果是，则继续往后遍历，如果不是，需要判断是一个数还是一个序列。使用双指针。


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        first, last = 0, 1
        result = []
        while last < len(nums):
            index = first
            while first + 1 == last:
                first += 1
                last += 1
            if first == index:
                result.append(str(first))
            else:
                result.append(str(index) + '->' + str(first))
            first = last
            last += 1
        return result


