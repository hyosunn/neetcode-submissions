class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        l, r = 0 ,len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if  s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l + 1, r + 1]













"""
    OPTIMAL NEETCODE SOLN O(n) time nad O(1) space:
 
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
"""