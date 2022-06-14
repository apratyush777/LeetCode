class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ""
        for i in word:
            if ord(i) < 97:
                s += i
            else:
                s += " "
        ans = list(set(s.split()))
        for i in range(len(ans)):
            ans[i] = int(ans[i])

        ans = list(set(ans))
        cnt = len(ans)
        return cnt
