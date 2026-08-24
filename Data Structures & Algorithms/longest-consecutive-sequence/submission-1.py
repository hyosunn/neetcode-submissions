class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        
        for n in nums:
            if n - 1 not in numSet:
                count = 1
                temp = n
                while temp + 1 in numSet:
                    count += 1
                    temp += 1
                ans = max(ans, count)
        
        return ans



