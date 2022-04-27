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
    
#This solution is O(n) and space is also O(n) 
#if we use sorting then space complexity is O(1) and time complexity is O(logN)
