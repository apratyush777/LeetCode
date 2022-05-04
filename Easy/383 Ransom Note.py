from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d=Counter(magazine)
        for i in ransomNote:
            if i in d:
                d[i]-=1
                if d[i]==0:
                    del(d[i])
            else:
                return False
            
        return True