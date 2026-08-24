class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r) // 2

            if target < nums[middle]:
                r = middle - 1
            elif target > nums[middle]:
                l = middle + 1
            else:
                return middle
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
            