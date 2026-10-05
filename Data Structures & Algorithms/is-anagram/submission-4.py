class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 0
            if t[i] not in tMap:
                tMap[t[i]] = 0

            sMap[s[i]] += 1
            tMap[t[i]] += 1
        
        return sMap == tMap
            



        
        
        
        
        
        
        
        
        
        



        """
        TIME EFFICIENT SOLN ----
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        return sMap == tMap

        SPACE EFFICIENT SOLUTION ------
        if sorted(s) == sorted(t):
            return True
        return False"""



