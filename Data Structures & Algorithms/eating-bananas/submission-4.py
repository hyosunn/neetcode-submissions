class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
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
