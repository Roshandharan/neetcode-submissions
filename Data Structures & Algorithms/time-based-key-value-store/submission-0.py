class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l = 0
        r = len(values)-1

        while l<=r:
            m = (l+r)//2
            if values[m][1]==timestamp:
                return values[m][0]
            elif values[m][1]<timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res
        
# make hashmap, store and list of list at every key,
# for set just update key else create new list for key
# for get, get all values of the key and do binary search, tc:(1), O(logn)
#sc= O(m*n)