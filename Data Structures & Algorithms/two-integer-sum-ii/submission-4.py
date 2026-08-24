class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while True:
            currSum = numbers[l] + numbers[r] 
            if currSum == target:
                return [l + 1, r + 1]
            elif currSum < target:
                l += 1
            else:
                r -= 1












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