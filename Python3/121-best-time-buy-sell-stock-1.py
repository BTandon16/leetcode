class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        buyPrice = prices[0]
        for i in range(1, len(prices)):
            if (buyPrice > prices[i]):
                buyPrice = prices[i]
            elif (buyPrice < prices[i]):
                profitMax = max(profitMax, prices[i] - buyPrice)
        return profitMax