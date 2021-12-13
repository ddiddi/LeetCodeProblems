# Prompt
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        int minprice = 90000
        int maxprofit = 0;
        for i, p in enumerate(prices):
            if p < minprice:
                minprice = p 
            elif p - minprice > maxprofit:
                maxprofit = p - minprice
        return maxprofit
