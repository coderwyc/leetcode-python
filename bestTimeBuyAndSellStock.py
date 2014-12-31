#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
#design an algorithm to find the maximum profit.

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
