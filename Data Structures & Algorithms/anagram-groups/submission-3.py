class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for w in strs:
            sortedStr = ''.join(sorted(w))
            map[sortedStr].append(w)
        return list(map.values())

        
        
        
        
        
        
        
        
        
            
        
        """
        NOTE FOR COMPLEXITY:
        m = # words and n = avg/max length of each word)

        also, sorted soln was faster for shorter strs, and count soln is 
        faster for longer strs. So in interview, try to address this caveat.
        """


        """
        SORTING SOLUTION ------ (Simpler, but not as optimal: 
                                O(m * n log n) time, and O(m * n) space)
        map = {}

        for s in strs:
            sortedStr = "".join(sorted(s))

            if sortedStr not in map:
                map[sortedStr] = []

            map[sortedStr].append(s)
        
        return list(map.values())
        """





        """
        OPTIMIZED COUNT SOLUTION ----- (O(m * n) time and O(26 * n) --> O(n) space)
        
        res = defaultdict(list)             # maps charCount to list of Anagrams

        for s in strs:
            count = [0] * 26                #index represents a...z in ascii and 
                                            #value @index is the # of occurences.
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)     #python dicts cannot have list as keys,
                                            #so tuple conversion goes first.

        return list(res.values())           #list call b/c res.values() 
                                            #returns dict.values() type, NOT list
        """