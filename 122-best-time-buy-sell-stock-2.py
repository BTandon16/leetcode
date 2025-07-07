class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        buyPrice = prices[0]
        for i in range(1, len(prices)):
            if (buyPrice < prices[i]):
                # Sell every day you make a profit, and buy on the same day 
                # (optimal for most total profit, not for least number of buy-sell for most total profit)
                profitMax += (prices[i] - buyPrice)
            buyPrice = prices[i]
        return profitMax