# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry, result = 1, []
        for num in reversed(digits):
            result.append((num + carry) % 10)
            carry = (num + carry) // 10
        if carry == 1:
            result.append(1)
        return result[::-1]
