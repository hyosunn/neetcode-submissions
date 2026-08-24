class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            if self.alnum(s[start]) and self.alnum(s[end]):
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1
            if not self.alnum(s[start]):
                start += 1
            if not self.alnum(s[end]):
                end -= 1

        return True
    
    def alnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord (c) <= ord('9'))














        """
        BUILT-IN METHOD--------- (Quick runtime, bad memory)
        cleanText = "".join([c for c in s if c.isalnum()]).lower()
        return cleanText == cleanText[::-1]
        """

        """
        CONSTANT MEMORY METHOD--------
        """