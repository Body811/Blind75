class Solution(object):
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p1= 0
        maxProfit = 0
        
        for p2 in range(1 , len(prices)):
            if prices[p2] > prices[p1]:
                profit = prices[p2] - prices[p1]
                maxProfit = max(profit,maxProfit)
            else:
                p1 = p2
                
        return maxProfit
        