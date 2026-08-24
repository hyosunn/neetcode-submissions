class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, max(piles)
        ans = maxK

        while minK <= maxK:
            midK = (minK + maxK) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / midK)
            if hours <= h:
                ans = min(ans, midK)
                maxK = midK - 1
            else:
                minK = midK + 1
            
        return ans


        
        
        
        
        
        
        
        
        
        
        
        
        
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
