class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans =[]
        map = {}
        for i in range(len(nums)):
            if target - nums[i] in map:
                ans.append(map[target-nums[i]])
                ans.append(i)
                return ans
            else:
                if nums[i] not in map:
                    map[nums[i]] = i
        
        
        
