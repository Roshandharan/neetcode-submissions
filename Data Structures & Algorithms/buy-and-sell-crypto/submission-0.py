class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0 ,1 #Left - buy, right - sell
        max_profit = 0

        while right < len(prices):

         if prices[right]>prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
         else:
            left = right
         right += 1
        return max_profit