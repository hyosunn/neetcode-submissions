class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        copy = set(nums)
        res = 0
        
        for n in copy:
            temp = n
            count = 1
            if temp - 1 not in copy:
                while temp + 1 in copy:
                    count += 1
                    temp += 1
                res = max(res, count)
        
        return res
            
            


        














"""     TIME: O(N) and SPACE: O(N)
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
"""



