# Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.
# Note:
#   1. The length of both num1 and num2 is < 5100
#   2. Both num1 and num2 contains only digits 0-9
#   3. Both num1 and num2 does not contain any leading zero
#   4. You must not use any built-in Biginteger library or convert the inputs to integer directly.


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result, carry, val = '', 0, 0
        for i in range(max(len(num1), len(num2))):
            if i < len(num1):
                val += int(num1[-i - 1])
            if i < len(num2):
                val += int(num2[-i - 1])
            result += str(val % 10)
            val //= 10
        if val != 0:
            result += str(val)
        return result[::-1]
