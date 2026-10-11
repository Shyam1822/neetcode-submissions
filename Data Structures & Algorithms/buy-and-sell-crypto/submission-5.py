class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        op = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                continue
            op = max(op,prices[i]-buy)
        return op