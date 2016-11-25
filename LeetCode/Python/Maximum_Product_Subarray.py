# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 思路：很简单的动态规划问题，要注意的地方是存在负数，因此状态方程分为两部分，
# 用数组positive_max[i]维护原始数组前i个数的子数组乘积中正数的最大值
# 用数组negative_min[i]维护原始数组前i个数的子数组乘积中负数的最小值
# if A[i] > 0:
#     positive_max[i] = max(positive_max[i-1] * A[i], A[i])
#     negative_min[i] = negative_min[i-1] * A[i]
# elif A[i] < 0:
#     positive_max[i] = negative_min[i - 1] * A[i]
#     negative_min[i] = min(positive_max[i - 1] * A[i], A[i])


class Solution(object):
    def maxProduct(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in A:
            local_max, local_min = max(x, local_max * x, local_min * x), min(x, local_max * x, local_min * x)
            global_max = max(global_max, local_max)
        return global_max




