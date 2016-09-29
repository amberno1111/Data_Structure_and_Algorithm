# Caculate the sum of two intergers a and b, but you are not allowed to use the operator + and -.
# Example:
# Given a = 1 and b = 2, return 3
# 解决办法就是利用二进制运算来模拟加法运算，或者可以直接利用python内置的sum函数
# 思路: 这里用到了一个半加法的思想, 即两位单独的位相加其结果可以用异或得到, 进位可以用与得到. 然后对于两个数字来说同样可以延伸这个思想.
# 举个例子: 11+5, 其二进制形式为11: 1011, 5: 0101
# 1. 那么两个位置都为1的地方就需要进位, 所以进位值就为0001. 原位置两个数相加的结果为那个位置值的异或即1110, 即两个位置值如果不一样就为1, 一样的话要么两个位置原来值都为0结果也为0, 要么进位, 那么结果依然是0.
# 2. 接下来就要把进位位和下一位相加, 所以进位值左移一位,即0001变为0010, 重复上面操作可得新的进位值为0010, 原位置异或(即相加)结果为1100.
# 3. 继续重复上面操作直到进位为0, 可得到最终结果10000, 即16


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])


class Solution1(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        result, carry = a ^ b, a & b
        while carry != 0:
            carry <<= 1
            result, carry = result ^ carry, result & carry
        return result
