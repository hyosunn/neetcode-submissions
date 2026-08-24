class Solution:
    def isPalindrome(self, s: str) -> bool:
        sortedStr = ''.join([c for c in s if c.isalnum()]).lower()
        return sortedStr == sortedStr[::-1]













        """
        BUILT-IN METHOD--------- (Quick runtime, bad memory)
        cleanText = "".join([c for c in s if c.isalnum()]).lower()
        return cleanText == cleanText[::-1]
        """

        """
        CONSTANT MEMORY METHOD-------- (Nested while-loop better b/c more edgecase-proof)
        def isPalindrome(self, s: str) -> bool:
            start, end = 0, len(s) - 1

            while start < end:
                while start < end and not s[start].isalnum():
                    start += 1

                while start < end and not s[end].isalnum():
                    end -= 1

                if s[start].lower() != s[end].lower():
                    return False

                start += 1
                end -= 1

            return True

        IF I NEED TO DEFINE MY OWN ALNUMERIC CHECKER USE ASCII------
        def alnum(self, c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord (c) <= ord('9'))
        """