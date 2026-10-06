class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1
        
        
        


        
        
        
        
        

        """
        OPTIMAL SOLUTION --------- Memorize this structure: VERY IMPORTANT
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2    #if integers bounded, do: m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1 
        """
            