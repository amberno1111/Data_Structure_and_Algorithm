# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process:
#   Starting with any positive integer, replace the number by the sum of the squares of its digits,
#   and repeat the process until the number equals 1 (Where it will stay), or ite loops endlessly in a cycle which does not include 1.
#   Thoes numbers for which this process ends in 1 are happy numbers.
# Example: 19 is a happy number
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = set()
        while True:
            result = 0
            for s in str(n):
                result += int(s) * int(s)
            n = result
            if result == 1:
                return True
            elif result in lookup:
                return False
            else:
                lookup.add(result)

