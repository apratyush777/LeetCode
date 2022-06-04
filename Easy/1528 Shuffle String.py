# 1st solution using dictionary

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        l = len(indices)
        for i in range(l):
            d[indices[i]] = s[i]
        ans = ''
        for i in range(l):
            ans += d[i]
        return ans


# 2nd solution

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        l = len(indices)
        d = [None]*l
        for i in range(l):
            d[indices[i]] = s[i]
        ans = ''
        for i in d:
            ans += i
        return ans
