class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        j = 0
        k = 0
        l = min(len(word1), len(word2))
        for i in range(2*l):
            if i % 2 == 0:
                ans += word1[j]
                j += 1
            else:
                ans += word2[k]
                k += 1
        if j != len(word1):
            for i in range(len(word1)-j):
                ans += word1[j]
                j += 1
        elif k != len(word2):
            for i in range(len(word2)-k):
                ans += word2[k]
                k += 1

        return ans
