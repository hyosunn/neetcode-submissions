class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanText = "".join([c for c in s if c.isalnum()]).lower()
        return cleanText == cleanText[::-1]













        """
        BUILT-IN METHOD---------
        cleanText = "".join([c for c in s if c.isalnum()]).lower()
        return cleanText == cleanText[::-1]
        """