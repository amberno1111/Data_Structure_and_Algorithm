# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# Example 1:
# Input: k = 3, n = 7
# Output:
# [[1,2,4]]
# Example 2:
# Input: k = 3, n = 9
# Output:
# [[1,2,6], [1,3,5], [2,3,4]]


# 思路：回溯法
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def search(start, cnt, sums, nums):
            if cnt > k or sums > n:
                return
            if cnt == k and sums == n:
                result.append(nums)
                return
            for i in range(start+1, 10):
                search(i, cnt+1, sums+i, nums+[i])
        search(0, 0, 0, [])
        return result
