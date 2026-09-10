class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      l,r =0,1
      max_profit = 0

      while r<len(prices):
         if prices[l]<prices[r]:
            profit = prices[r]-prices[l]
            max_profit = max(profit, max_profit)
         else:
            l =r
         
         r+=1
      
      return max_profit
     

#     Dp Solution
#      min_price = float('inf')
#      max_profit = 0
#
#      for price in prices:
#         if price<min_price:
#            min_price = price
#         
#         profit = price - min_price
#
#         max_profit = max(max_profit, profit)
#      
#     return max_profit
   
# tc=O(n)
# sc=O(1)

# Left buy, right sell