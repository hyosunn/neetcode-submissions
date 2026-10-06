class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        tempSet = set()

        while r < len(s):
            while s[r] in tempSet:
                tempSet.remove(s[l])
                l += 1

            tempSet.add(s[r])
            r += 1
            res = max(res, len(tempSet))

        return res
            
            
            













        

    """
    OPTIMAL SOLUTION (O(n) time and O(m) space where m = len(largest substring))
    Note: Could also use hashmaps but set is more fitting.

    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res"""