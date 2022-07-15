class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i, j = 0, 0
        l = len(s)
        d = {}
        op = []

        for it in p:
            if it in d:
                d[it] += 1
            else:
                d[it] = 1
        cnt = len(d)
        while j < l:
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    cnt -= 1

            if j-i+1 < len(p):
                j += 1
            else:
                if cnt == 0:
                    op.append(i)
                if s[i] in d:
                    d[s[i]] += 1
                    if d[s[i]] == 1:
                        cnt += 1
                i += 1
                j += 1

        return op
