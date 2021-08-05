"""
LC 121
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        O(n) solution
        """

        max_profit = 0
        best_possible = 0
        for i in range(len(prices)-2, -1, -1):
            gain = prices[i+1] - prices[i]
            best_possible = max(best_possible + gain, 0)
            max_profit = max(max_profit, best_possible)


        return max_profit


        """
        O(n^2) Solution
        max_profit = 0
        for i in range(len(prices)):
            curr = prices[i]
            for j in range(i + 1, len(prices)):
                curr_profit = prices[j] - prices[i]
                max_profit = max(max_profit, curr_profit)

        return max_profit
        """
