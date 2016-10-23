# Given an array of integers A and let n to be its length.
# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
# Calculate the maximum value of F(0), F(1), ..., F(n-1).
# Note:
# n is guaranteed to be less than 105.
# Example:
# A = [4, 3, 2, 6]
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
# 思路: 假设数组A的长度为5，其旋转函数F的系数向量如下所示：
# 0 1 2 3 4
# 1 2 3 4 0
# 2 3 4 0 1
# 3 4 0 1 2
# 4 0 1 2 3
# 用每一行系数与其上一行做差，差值恰好为sum(A) - size * A[size - x]，其中x为行数
# 因此，通过一次遍历即可求出F(0), F(1), ..., F(n-1)的最大值。


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size, sums = len(A), sum(A)
        sumn = sum(x * n for x, n in enumerate(A))
        ans = sumn
        for x in range(size - 1, 0, -1):
            sumn += sums - size * A[x]
            ans = max(ans, sumn)
        return ans
