class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanText = "".join([c for c in s if c.isalnum()]).lower()
        start, end = 0, len(cleanText) - 1

        while start < end:
            if cleanText[start] != cleanText[end]:
                return False
            start += 1
            end -= 1
        return True