# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# 思路：贪心法则，从前向后遍历数组，只要当前的价格高于前一天的价格，就可以算入收益。比如在 i 天买进，j 天卖出，如果有j+1 天的价格高于 j天，那么肯定是从i到j+1天，同样的，如果有i+1的价格低于i天，肯定是从i-1到j天利润更高，所以对应每一段，我们只需要找到波峰和波谷相减就行，最后把利润累加。


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]
        return profit

