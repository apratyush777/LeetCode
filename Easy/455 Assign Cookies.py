class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gl = len(g)
        sl = len(s)
        i, j = gl-1, sl-1
        cnt = 0

        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                i -= 1
                j -= 1
                cnt += 1
            else:
                i -= 1

        return cnt
