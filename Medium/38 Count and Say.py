def pattern(temp):
    cnt = 1
    ans = ''
    for i in range(len(temp)-1):
        cur = temp[i]
        nxt = temp[i+1]
        if cur == nxt:
            cnt += 1
        else:
            ans += str(cnt)
            ans += cur
            cnt = 1

    if cur == nxt:
        ans += str(cnt)
        ans += cur
    else:
        ans += str(cnt)
        ans += nxt
    return ans


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            temp = '11'
            for i in range(n-2):
                temp = pattern(temp)
            return temp
