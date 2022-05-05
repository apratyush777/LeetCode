class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1={}
        d2={}
        li=s.split()
        if len(pattern) == len(li):
            for i in range(min(len(pattern),len(li))):
                if pattern[i] not in d1 and li[i] not in d2:
                    d1[pattern[i]] = li[i]
                    d2[li[i]] = pattern[i]
                elif (pattern[i] in d1 and d1[pattern[i]]!=li[i]) or (li[i] in d2 and d2[li[i]]!=pattern[i]):
                    return False
            
            return True
        else:
            return False