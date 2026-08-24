class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            maxP = max(maxP, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return maxP
        
        
        
        
        

        
        
        
        
        
        
        
        
    """ OPTIMAL SLIDOW SOLN: (O(n) time and O(1) space)
        l, r = 0, 1
        maxProf = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit =  prices[r] - prices[l]
                maxProf = max(maxProf, profit)
            else:
                l = r
            r += 1
        
        return maxProf
    """
