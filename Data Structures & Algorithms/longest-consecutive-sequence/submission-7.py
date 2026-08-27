class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in numSet:
            if n - 1 not in numSet:
                temp, total = n, 1
                while temp + 1 in numSet:
                    total += 1
                    temp += 1
                res = max(res, total)
        
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



