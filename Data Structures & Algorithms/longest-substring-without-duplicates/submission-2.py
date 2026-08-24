class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = defaultdict(int)
        l, r = 0, 0
        ans = 0
        
        while r < len(s):
            if s[r] not in map:
                map[s[r]] += 1
                ans = max(ans, len(map))
                r += 1
            else:
                map.pop(s[l])
                l += 1
        return ans
