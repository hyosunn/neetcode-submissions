class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cMap = defaultdict(int)
        count = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            cMap[n] += 1
        
        for i, v in cMap.items():
            count[v].append(i)

        res = []
        for l in range(len(count) - 1, -1 ,-1):
            
            for x in count[l]:
                res.append(x)
                if len(res) == k:
                    return res

            

        













"""
    BUCKET SORT SOLUTION in O(n) time and space. 

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq) - 1, 0 , -1): # doing count[::-1] creates a copy
        for n in freq[i]:                    which is not optimal space usage.
            res.append(n)
            if len(res) == k:
                return res
"""
    



