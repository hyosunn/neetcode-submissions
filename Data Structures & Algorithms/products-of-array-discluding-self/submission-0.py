class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        countZero = 0
        ans = []

        for n in nums:
            if n != 0:
                product *= n
            else:
                countZero += 1
        
        if countZero > 1:
            ans = [0 for n in nums]
        elif countZero == 1:
            for n in nums:
                if n != 0:
                    ans.append(0)
                else:
                    ans.append(product)
        else:
            for n in nums:
                ans.append(int(product / n))
            
        return ans

        
    

        