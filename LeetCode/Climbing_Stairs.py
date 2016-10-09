# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?


# 思路: 动态规划,f(n) = f(n-1) + f(n-2)
# LeetCode上提交, 遇到TLE
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# 思路: 实际上是一个斐波那契数列
class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current
