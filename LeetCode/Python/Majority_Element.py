# Given an array of size n, find the majority element.
# The majority element is the element that appears more than n/2 times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# 思路:每找出两个不同的element，则成对删除，最终剩下的一定就是所求的。
# 可扩展到 n/k 的情况，每 k 个不同的element一起删除
# 注意元素E会出现超过 n/k次
# 为了简化问题，我们假设 n/k可以整除，因此E出现的次数至少是 n/k + 1 次
# 我们把整个数组分成 n/k 组，每一组里面都有 k 个元素，它们各不相同
# 假设E能够均匀的分配到每一个数组里面，也就是说 前面 n/k -1 组里面，肯定有每一组里面都有一个 E 元素
# 而最后一组里面，肯定会出现两个 E 元素，而其他的则互不相同，可知 E 就是majority element。
# 在算法中，我们寻找k个不同的元素，并把他们分为一组，并删除
# 注意，E 不一定会被均匀分配，因此最后剩下的那个组里面 E 有可能会出现超过2次。


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, candidate = 0, 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            elif candidate == nums[i]:
                count += 1
            else:
                count -= 1
        return candidate
