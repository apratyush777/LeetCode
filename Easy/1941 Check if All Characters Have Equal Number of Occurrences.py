class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        temp = d[i]

        for i in d:
            if d[i] != temp:
                return False
        return True
