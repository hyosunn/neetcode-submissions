class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, v in enumerate(nums):
            if target - v in map:
                return [map[target - v], i]
            map[v] = i

        
        
        
        
        
        
        
        
        
        
        
        """
        OPTIMAL SOLN FROM NEETCODE HIMSELF------
        
        prevMap = {} 
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        """
        
        
        
