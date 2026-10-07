class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 1
        cMap = defaultdict(int)
        freq = 0 

        while r < len(s):
            cMap[s[r]] += 1
            freq = max(freq, cMap[s[r]])

            while r - l + 1 - freq > k:
                cMap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1

        return res


            



        
        
        
        
        
        
        




        
        
        
        """
        Almost OPTIMAL SOLN (O(n) time and O(m) space
                             Where n is len(s) and m is # unique chars in the string))
              - This method uses hashmap for counting occurences

        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
        """



            




