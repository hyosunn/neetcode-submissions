class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        



        """
        TIME EFFICIENT SOLN"
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        return sMap == tMap"""

