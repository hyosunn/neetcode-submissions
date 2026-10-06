class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            hr = 0
            for p in piles:
                hr += math.ceil(p / m)
            if hr <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
            




        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        OPTIMAL SOLUTION (O(nlogm) time and O(1) space
                          where n is size of input array and m is max value
                          in the array)
                          
        minK, maxK = 1, max(piles)
        ans = maxK

        while minK <= maxK:
            midK = (minK + maxK) // 2
            count = 0
            for i in piles:
                count += math.ceil(i / midK)
            
            if count <= h:
                ans = min(ans, midK)
                maxK = midK - 1
            else:
                minK = midK + 1
        
        return ans
        """
