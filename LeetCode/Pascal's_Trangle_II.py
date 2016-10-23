# Given an index k, return kth row of the Pascal's triangle.
# For example, given k = 3,
# Return [1, 3, 3, 1]

# Time: O(n^2)
# 我们可以发现帕斯卡三角的规律是这样的，假定你要求k=3时的列表，
# 创建一个有4个元素的[0, 0, 0, 0]，把第一个元素设置为1，[1, 0, 0, 0]
# 把第一个元素的值加到第二个数上面可得，[1, 1, 0, 0],左边的两个数恰好是k=1时的值
# 把第一个元素的值加到第二个数上面，把原来的第二个元素的值(是1，而不是2)加到第三个元素上得到[1, 2, 1, 0],左边三个数恰好是k=2时的值
# 再然后把第一个元素的值加到第二个数上面，把原来的第二个元素的值(是2，而不是3)加到第三个元素上，
# 把原来的第三个元素(是1，而不是3)加到第四个元素上得到[1, 3, 3, 1]正好就可以得到k=3时候的值
# 所以不断的对整个列表进行遍历和相加就可以得到结果


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            old = result[0] = 1
            for j in range(1, i + 1):
                old, result[j] = result[j], old + result[j]
        return result


    # 从后往前遍历更好,不需要额外的变量来保存之前的值
    def getRow(self, rowIndex):
        result = [0] * (rowIndex + 1)
        result[rowIndex], result[0] = 1, 1
        for i in range(rowIndex):
            k = rowIndex - 1
            while k > 0:
                result[k] += result[k - 1]
                k -= 1
        return result


