class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}
        a1 = s1.split()
        a2 = s2.split()
        for i in a1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in a2:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        res = []
        for i in d:
            if d[i] == 1:
                res.append(i)

        return res
