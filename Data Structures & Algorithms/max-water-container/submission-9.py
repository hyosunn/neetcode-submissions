class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1
        res = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r-= 1
        
        return res

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        """ O(n) time and O(1) space
        ans = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            ans = max(ans, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ans
        """
