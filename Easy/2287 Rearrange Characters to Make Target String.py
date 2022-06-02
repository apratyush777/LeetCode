class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        t = {}
        for i in target:
            if i not in t:
                t[i] = 1
            else:
                t[i] += 1

        minn = 999999999
        for i in target:
            if i not in d:
                return 0
            else:
                minn = min(minn, d[i]//t[i])
        return minn
