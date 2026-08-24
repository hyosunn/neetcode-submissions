class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        maxHeight = 0

        while l < r:
            maxHeight = max(maxHeight, min(height[l], height[r]))

            if height[l] < maxHeight:
                ans += maxHeight - height[l]
            elif height[r] < maxHeight:
                ans += maxHeight - height[r]

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans



        