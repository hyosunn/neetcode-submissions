class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, v in enumerate(nums):
            map[v] = i
        
        for i, v in enumerate(nums):
            if target - v in map and map[target - v] != i:
                return [i, map[target - v]]
                
        

        
        
        
        
        
        
        
        
        
        



        
        """
        OPTIMAL SOLN FROM NEETCODE HIMSELF------
        
        prevMap = {} 
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        """
        
        
        
