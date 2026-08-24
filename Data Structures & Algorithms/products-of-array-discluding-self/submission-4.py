class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pre = 1
        for i, n in enumerate(nums):
            ans[i] *= pre
            pre *= n
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        
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
        
    

        