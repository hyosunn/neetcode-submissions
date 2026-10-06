class Solution:
    def findMin(self, nums: List[int]) -> int: #Look for rotation point
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1   # m is in the left run, min is strictly right of m
            else:
                r = m       # m is in the right run, m itself could be the min
        
        return nums[l]
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        """ O(log n) time and O(1) space
            - The idea here is if left side sorted, then min must 
            - be in the right. also, if ascending order, then that 
            - means if nums[l] < nums[r] then we already have an
            - array (or subarray) thats in ascending sorted order!

        
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
                
        return res
        """