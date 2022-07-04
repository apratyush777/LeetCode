class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for i in words:
            flag = False
            if len(i) < len(pref):
                continue
            for j in range(len(pref)):
                if i[j] == pref[j]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                cnt += 1
        return cnt
