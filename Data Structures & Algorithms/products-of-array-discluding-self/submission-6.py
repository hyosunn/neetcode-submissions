class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] *= pre 
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= post 
            post *= nums[i]
        
        return res
            


            











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
        
    

        