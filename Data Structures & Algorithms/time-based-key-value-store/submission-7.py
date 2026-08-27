class TimeMap:

    def __init__(self):
        self.pairs = defaultdict(list) # key = key, value = [ [val1, timestamp1] ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        timeVal = [value, timestamp]
        self.pairs[key].append(timeVal)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.pairs:
            return res

        if timestamp >= self.pairs[key][-1][1]:
            return self.pairs[key][-1][0]

        l , r = 0, len(self.pairs[key]) - 1
        while l <= r:
            m = (l + r) // 2

            if self.pairs[key][m][1] <= timestamp:
                res = self.pairs[key][m][0]
                l = m + 1
            else:
                r = m - 1

        return res



        
