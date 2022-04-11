class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for i, j in zip(s, t):
            if i not in d1 and j not in d2:
                d1[i] = j
                d2[j] = i

            elif d1.get(i) != j or d2.get(j) != i:
                return False

        return True
