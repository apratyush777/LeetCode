from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = Counter(s)
        for i in t:
            if i in d:
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
            else:
                return False
        if len(d) == 0:
            return True
        return False
