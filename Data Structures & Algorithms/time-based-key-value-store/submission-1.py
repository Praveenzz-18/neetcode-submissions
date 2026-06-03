class TimeMap:

    def __init__(self):
        self.hashTable = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hashTable.get(key, []) == []:
            self.hashTable[key] = []

        self.hashTable[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        keyList = self.hashTable.get(key, [])
        res = ""
        l = 0
        r = len(keyList) - 1
        while l <= r:
            m = (r - l) // 2 + l

            if keyList[m][1] <= timestamp:
                res = keyList[m][0]
                l = m + 1
            else:
                r = m - 1

        return res        
