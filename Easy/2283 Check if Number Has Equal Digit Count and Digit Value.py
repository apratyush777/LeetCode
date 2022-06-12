class Solution:
    def digitCount(self, num: str) -> bool:
        if len(num) == 1:
            return False
        d = {}
        for i in num:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in range(len(num)):
            if str(i) not in d:
                d[str(i)] = 0
        # print(d)
        l = len(num)
        for i in range(l):
            if str(i) in d:
                if int(num[i]) != d[str(i)]:
                    return False
            else:
                return False

        return True
