class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i, j = 0, 0
        d = {}
        cnt = 0
        ans = 0
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
                cnt += 1
            else:
                d[s[j]] += 1
            if j-i+1 < 3:
                j += 1
            else:
                if cnt == 3:
                    ans += 1
                d[s[i]] -= 1

                if d[s[i]] == 0:
                    cnt -= 1
                    del(d[s[i]])
                i += 1
                j += 1
        return ans
