class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for s in strs:
            sortedStr = "".join(sorted(s))

            if sortedStr not in map:
                map[sortedStr] = []

            map[sortedStr].append(s)
        
        return list(map.values())        