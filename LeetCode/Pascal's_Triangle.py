# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,
# Return
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# 根据帕斯卡三角形的性质 C(n+1, i) = C(n, i) + C(n-1, i)
# 即可以通过N-1层来求N层
# 方法是在左右边各加一个0构造两个列表，然后将两个列表相加即可得到N层
# 例如，已知[1, 2, 1]，左右边各加一个0得到两个列表[0, 1, 2, 1]和[1, 2, 1, 0]
# 两个列表各项相加即可得[1, 3, 3, 1]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            result, res = [[1]], [1]
            for i in range(1, numRows):
                res = [sum(i) for i in zip([0] + res, res + [0])]
                result.append(res)
            return result
