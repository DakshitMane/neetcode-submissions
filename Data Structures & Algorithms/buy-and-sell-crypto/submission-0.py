class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, minVal = 0, float('inf')
        for price in prices:
            if price < minVal:
                minVal = price
            profit = price - minVal

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit