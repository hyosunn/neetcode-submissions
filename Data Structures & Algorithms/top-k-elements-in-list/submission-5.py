class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for a, b in count.items():
            freq[b].append(a)
        
        ans= []
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                ans.append(v)
                if len(ans) == k:
                    return ans




        












"""
    BUCKET SORT SOLUTION in O(n) time and space. 

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq) - 1, 0 , -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
"""
    



