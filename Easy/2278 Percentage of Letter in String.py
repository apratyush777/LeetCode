import math


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = 0
        l = 0
        for i in s:
            if i == letter:
                cnt += 1
            l += 1
        return math.floor((cnt/l)*100)
