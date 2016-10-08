# Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result, carry = '', 0
        for i in range(max(len(a), len(b))):
            if i < len(a):
                carry += int(a[-(i+1)])
            if i < len(b):
                carry += int(b[-(i+1)])
            result += str(carry % 2)
            carry //= 2
        if carry == 1:
            result += '1'
        return result[::-1]
