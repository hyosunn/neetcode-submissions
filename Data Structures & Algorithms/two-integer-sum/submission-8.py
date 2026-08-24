class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]], i]
            map[nums[i]] = i
        
        
        
        
        
        
        
        
        
        
        
        
        """
        OPTIMAL SOLN FROM NEETCODE HIMSELF------
        
        prevMap = {} 
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        """
        
        
        
