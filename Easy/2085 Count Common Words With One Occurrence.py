class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = {}
        d2 = {}
        for i in words1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in words2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        cnt = 0

        for i in d1:
            if d1[i] == 1 and i in d2:
                if d2[i] == 1:
                    cnt += 1

        return cnt
