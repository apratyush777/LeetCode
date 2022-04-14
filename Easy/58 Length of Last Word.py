class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        e = s.strip()
        # print(s)
        cnt = 0
        if len(e) == 1:
            return 1
        else:
            for i in range(len(e)-1, -1, -1):
                if e[i] != " ":
                    cnt += 1
                    # print(i)
                else:
                    break

        return cnt
