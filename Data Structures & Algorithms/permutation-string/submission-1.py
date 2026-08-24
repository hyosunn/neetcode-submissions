class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        s1Count = defaultdict(int)
        for s in s1:
            s1Count[s] += 1

        while r < len(s2):
            count = defaultdict(int)
            for i in range(l, r + 1):
                count[s2[i]] += 1
            
            if count == s1Count:
                return True
            r += 1
            l += 1
        
        return False


