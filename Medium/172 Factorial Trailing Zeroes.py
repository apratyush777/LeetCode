# 1st method using mathematics
import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        temp = math.factorial(n)
        cnt = 0
        while temp > 0:
            if temp % 10 == 0:
                cnt += 1
                temp = temp//10

            else:
                return cnt

        return cnt

# 2nd method using string


class Solution:
    def trailingZeroes(self, n: int) -> int:
        temp = str(math.factorial(n))
        i = len(temp)-1
        cnt = 0
        while temp[i] == '0':
            cnt += 1
            i -= 1

        return cnt
