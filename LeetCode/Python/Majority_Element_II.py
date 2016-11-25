# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
# 思路：moore投票算法，已知数组中至多可能出现2个出现次数超过⌊ n/3 ⌋ 的众数，记变量n1, n2为候选众数，c1, c2为它们对应的出现次数，遍历数组，记当前数字为num，若num与n1或n2相同，则将其对应出现次数加1；否则，若c1或c2为0，将其置1，对应的候选众数为num，否则c1与c2分别减1，最后再统计一次候选众数在数组中出现的次数，若满足要求，则返回之


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n1, n2 = None, None
        c1, c2 = 0, 0
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1
        return [n for n in (n1, n2) if nums.count(n) > len(nums) // 3]





