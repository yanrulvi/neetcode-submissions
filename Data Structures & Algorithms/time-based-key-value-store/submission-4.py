class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.store[key]) - 1
        while left <= right:
            m = (left + right) // 2
            if self.store[key][m][1] <= timestamp:
                left = m + 1
            else:
                right = m - 1
        
        if right == -1:
            return ""
        return self.store[key][right][0]
