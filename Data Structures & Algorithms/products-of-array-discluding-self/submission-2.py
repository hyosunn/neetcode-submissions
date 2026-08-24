class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        ans = [1] * len(nums)
        
        for i, v in enumerate(nums):
            ans[i] *= pre
            pre *= v
        
        for r in range(len(nums) - 1, -1, -1):
            ans[r] *= post
            post *= nums[r]
        
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
        
    

        