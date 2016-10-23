# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
# In this case, no transaction is done, i.e. max profit = 0
# 思路: 对于每一笔交易 假设是从i天买入 j天卖出 ，如果有j+1天的价格高于j天，所以肯定是从i到j+1利润更高，同样的如果有第i-1天价格比第i天更低，肯定是从i-1天到j天利润更高。所以是不是对于每一段我们只用找到波谷和波峰，相减就可以了呢？
# 再分析一下，可以推出一个非常简单的式子，只要后项比前项大，这部分值就一定可以变为利润，即：
# sum = sum+a[i+1]-a[i](if a[i+1]>a[i])


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit, min_price = 0, prices[0]
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

