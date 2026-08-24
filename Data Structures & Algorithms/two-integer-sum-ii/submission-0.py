class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if l < r and numbers[r] > target - numbers[l]:
                r -= 1
            elif l < r and numbers[l] < target - numbers[r]:
                l += 1
            
            if numbers[r] + numbers[l] == target:
                return [l + 1, r + 1]
