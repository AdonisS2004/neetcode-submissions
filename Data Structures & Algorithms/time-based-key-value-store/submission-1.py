class TimeMap:

    def __init__(self):
        self.kv = dict() # key:list[tuple(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # print(f"get({key}, {timestamp}) --> print({self.kv=})")
        # base cases
        if key not in self.kv:
            return ""
        if not self.kv[key]:
            return ""
        if self.kv[key][0][0] > timestamp:
            return ""


        n = len(self.kv[key])
        l, r = 0, n
        while l < r:
            mid = (l+r)//2
            time, val = self.kv[key][mid]
            if time == timestamp:
                return val
            if time > timestamp:
                r = mid
            else:
                l = mid + 1
        return self.kv[key][r-1][1]

