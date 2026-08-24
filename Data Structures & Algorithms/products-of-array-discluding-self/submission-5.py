class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        prefix = 1
        for i, v in enumerate(nums):
            ans[i] *= prefix
            prefix *= v
        
        postfix = 1
        for j in range(len(nums) - 1, -1 , -1):
            ans[j] *= postfix
            postfix *= nums[j]
        
        return ans
        


            











        """ OPTIMAL SOLN NO DIVISION (O(n) time and O(1) memory):

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        """
        
    

        