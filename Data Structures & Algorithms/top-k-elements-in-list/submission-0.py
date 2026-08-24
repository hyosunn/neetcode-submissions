class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kMap = defaultdict(int)
        result = []

        for n in nums:
            kMap[n] += 1

        for i in range(k):
            maxKey = max(kMap.keys(), key=kMap.get)
            kMap.pop(maxKey)
            result.append(maxKey)
        
        return result

