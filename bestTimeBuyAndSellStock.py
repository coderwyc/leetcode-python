class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, price):
        begin = 0
        end = 0
        profit = 0
        for end in range(len(price)):        
            delta = price[end] - price[begin]
            if delta < 0:
                begin = end
            if delta >= profit:
                profit = delta
        return profit
