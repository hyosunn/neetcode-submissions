class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1
            if not s[start].isalnum():
                start += 1
            if not s[end].isalnum():
                end -= 1

        return True
        













        """
        BUILT-IN METHOD--------- (Quick runtime, bad memory)
        cleanText = "".join([c for c in s if c.isalnum()]).lower()
        return cleanText == cleanText[::-1]
        """

        """
        CONSTANT MEMORY METHOD--------
        """