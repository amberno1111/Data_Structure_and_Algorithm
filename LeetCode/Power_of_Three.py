# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# 给定一个整数，编写一个函数判断它是否是3的幂
# -------------------------------------------------------------------


import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n == 3 ** round(math.log(n, 3))
