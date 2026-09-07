class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #6/9/26

        op=0

        cur_buy = prices[0]
        for i in prices[1:]:
            if cur_buy>i:
                cur_buy = i
                continue
            if i-cur_buy>op:
                op = i-cur_buy
        return op