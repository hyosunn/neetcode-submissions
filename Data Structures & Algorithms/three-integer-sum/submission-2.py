class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                target = nums[l] + nums[r] + v
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    ans.append([nums[l], nums[r] , v])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans

        
    
        
        
        
        
        
        



        
        
        
    """ OPTIMAL SOLUTION (O(n^2) time and O(1) space)
        ans = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
        
    """